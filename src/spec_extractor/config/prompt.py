from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

def get_extraction_prompt(output_parser: PydanticOutputParser) -> ChatPromptTemplate:
    system_template = """
    You are an expert Technical Data Extractor specializing in renewable energy hardware.
    Your goal is to parse solar panel manual text and extract technical specifications into a structured JSON format.

    ### Extraction Rules:
    1. **Normalization**: Map diverse terms to standard fields:
       - 'Rated Power', 'Nominal Power', 'Output Power', 'Maximum Output', and 'Module Rating' -> `rated_power_w`[cite: 6, 25, 42, 62, 76, 93].
       - 'Vmp' or 'Nominal Voltage' -> `nominal_voltage_v`[cite: 62, 93].
       - 'Voc' or 'Max Voltage' -> `max_voltage_v`[cite: 6, 27].
       - 'Imp' -> `operational_amperage_a`.
    2. **Unit Conversion**: 
       - Always return numbers (int/float) without units (e.g., "310W" becomes 310).
       - If power is in kW, convert to Watts (multiply by 1000).
    3. **Dimension Splitting**: 
       - If dimensions are provided as a string like '1900x1130x40 mm', split them into height_mm (1900), width_mm (1130), and depth_mm (40).
    4. **Missing Data**: 
       - If a field is not explicitly mentioned in the text, return null. Do not hallucinate values.
    5. **Model Name**: 
       - Extract the full product name usually found at the beginning of the manual[cite: `Solnix Horizon`, `Aurelios Prime`, `TerraVolt Edge`].

    {format_instructions}
    """

    user_template = "Extract the specifications from the following manual text:\n\n{text}"

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", user_template),
    ])
    
    return prompt.partial(format_instructions=output_parser.get_format_instructions())