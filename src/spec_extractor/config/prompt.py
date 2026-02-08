from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser


def get_extraction_prompt(output_parser: PydanticOutputParser) -> ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages([])
    return prompt.partial(format_instructions=output_parser.get_format_instructions())

