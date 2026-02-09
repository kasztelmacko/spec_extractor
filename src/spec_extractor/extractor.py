from src.spec_extractor.config.models import SolarPanelSpecs
from src.spec_extractor.config.config import OllamaConfig
from src.spec_extractor.config.prompt import get_extraction_prompt

from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser

from pathlib import Path
import fitz  # PyMuPDF


class TechnicalSpecificationExtractor:
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

    def extract(self, file_path: str) -> SolarPanelSpecs:
        text = self._extract_text_from_pdf(file_path=file_path)
        return self._extract_specification_from_text(text=text)

    def _extract_text_from_pdf(self, file_path: str | Path) -> str:
        """Extract text from PDF using PyMuPDF library."""
        pdf_path = str(file_path) if isinstance(file_path, Path) else file_path
        doc = fitz.open(pdf_path)
        text_parts = []
        
        for page in doc:
            text_parts.append(page.get_text())
        doc.close()
        
        return "\n".join(text_parts)