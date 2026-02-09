from pathlib import Path
from src.spec_extractor.extractor import TechnicalSpecificationExtractor

def main():
    extractor = TechnicalSpecificationExtractor(
        model_name="llama3.2",
        if_use_api=False,
        api_url=None,
        base_url=None
    )
    
    pdf_path = Path("data/sample_manuals/manual_1_cleaned.pdf")
    
    extracted_text = extractor._extract_text_from_pdf(file_path=pdf_path)
    print(extracted_text)

if __name__ == "__main__":
    main()

