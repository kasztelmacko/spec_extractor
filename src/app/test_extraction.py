from pathlib import Path
import os

from src.spec_extractor.extractor import TechnicalSpecificationExtractor


def main():
    model_name = os.getenv("OLLAMA_MODEL", "llama3.2")

    extractor = TechnicalSpecificationExtractor(
        model_name=model_name,
        if_use_api=False,
        api_url=None,
        base_url=None,
    )

    pdf_path = Path("data/sample_manuals/manual_1_cleaned.pdf")

    specifics = extractor.extract(file_path=pdf_path)
    print(specifics)


if __name__ == "__main__":
    main()

