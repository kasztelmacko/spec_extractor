from src.spec_extractor.config.models import SolarPanelSpecs
from src.spec_extractor.config.config import OllamaConfig
from src.spec_extractor.config.prompt import get_extraction_prompt

from langchain_community.chat_models import ChatOllama
from langchain.output_parsers import PydanticOutputParser


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

    def extract(self, pdf_spec_path: str) -> SolarPanelSpecs:
        text = self._extract_text_from_pdf(pdf_spec_path=pdf_spec_path)
        return self._extract_specification_from_text(text=text)