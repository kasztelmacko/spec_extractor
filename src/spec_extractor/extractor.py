from typing import Any


from src.spec_extractor.config.models import SolarPanelSpecs
from src.spec_extractor.config.config import OllamaConfig
from src.spec_extractor.config.prompt import get_extraction_prompt

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser

from pathlib import Path
import re
import fitz
import pandas as pd


class TechnicalSpecificationExtractor:
    """Extracts technical specifications from solar panel PDF manuals using LLM.
    
    This class handles the complete extraction pipeline: PDF text extraction,
    text cleaning, and AI-powered specification extraction using Ollama models.
    
    Args:
        model_name: Name of the Ollama model to use for extraction (e.g., 'llama3.2', 'mistral').
        if_use_api: Whether to use an external API endpoint instead of local Ollama instance.
        api_url: API URL endpoint when if_use_api is True. If None and if_use_api is True, 
            will raise an error.
        base_url: Base URL for local Ollama instance. If None, will check OLLAMA_HOST 
            environment variable or default to 'http://localhost:11434'.
    """
    def __init__(
        self,
        model_name: str,
        if_use_api: bool,
        api_url: str | None,
        base_url: str | None,
    ):
        self.config = OllamaConfig(
            model_name=model_name,
            if_use_api=if_use_api,
            api_url=api_url,
            base_url=base_url
        )
        self.llm = ChatOllama(
            model=self.config.model_name,
            base_url=self.config.get_ollama_url(),
        )
        self.output_parser = PydanticOutputParser(pydantic_object=SolarPanelSpecs)
        self.prompt = get_extraction_prompt(output_parser=self.output_parser)

    def extract(self, file_path: str) -> pd.DataFrame:
        """Extracts solar panel specifications from a PDF file and returns them as a DataFrame.

        The pipeline goes through following steps:
            1. reads and concatenates all PDF pages
            2. cleans the text
            3. runs the LLM to get a SolarPanelSpecs Pydantic model
            4. converts the model into a DataFrame with columns: Specification, Value
        """
        text = self._extract_text_from_pdf(file_path=file_path)
        text_cleaned = self._clean_extracted_text(text=text)
        specifications = self._extract_specification_from_text(text=text_cleaned)
        return self._dump_specifications_to_dataframe(specifications=specifications)

    def _extract_text_from_pdf(self, file_path: str | Path) -> str:
        """Extracts raw text content from all pages of a PDF file."""
        pdf_path = str(file_path) if isinstance(file_path, Path) else file_path
        doc = fitz.open(pdf_path)
        text_parts = []
        
        for page in doc:
            text_parts.append(page.get_text())
        doc.close()
        
        return "\n".join(text_parts)

    def _clean_extracted_text(self, text: str) -> str:
        """Cleans extracted text by removing non-ASCII characters, collapsing whitespace, and removing empty lines."""
        text = text.encode('ascii', 'ignore').decode('ascii')
        lines = text.split('\n')
        cleaned_lines = []
        for line in lines:
            line = re.sub(r'[ \t]+', ' ', line)
            line = line.strip()
            if line:
                cleaned_lines.append(line)

        return '\n'.join(cleaned_lines)

    def _extract_specification_from_text(self, text: str) -> SolarPanelSpecs:
        """Uses LLM to extract structured specifications from cleaned text.
        Returns a validated SolarPanelSpecs Pydantic model parsed from the LLM response.
        """
        formatted_prompt = self.prompt.format_messages(text=text)
        response = self.llm.invoke(formatted_prompt)
        return self.output_parser.parse(response.content)

    def _dump_specifications_to_dataframe(self, specifications: SolarPanelSpecs) -> pd.DataFrame:
        """Convert a SolarPanelSpecs object into a DataFrame (Specification, Value)."""
        data = specifications.model_dump(exclude_none=True)
        return pd.DataFrame(list[tuple[str, Any]](data.items()), columns=["Specification", "Value"])