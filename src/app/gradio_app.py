import os
import pandas as pd
import gradio as gr
from src.spec_extractor.extractor import TechnicalSpecificationExtractor


def extract_specifications(pdf_file: str | None) -> pd.DataFrame:
    """Extract specifications from uploaded PDF file."""
    if pdf_file is None:
        return pd.DataFrame(columns=["Specification", "Value"])

    try:
        return EXTRACTOR.extract(file_path=pdf_file)

    except Exception as e:
        return pd.DataFrame(
            {
                "Specification": ["Error"],
                "Value": [f"Error extracting specifications: {str(e)}"],
            }
        )


with gr.Blocks(title="Solar Panel Specification Extractor") as demo:
    with gr.Row():
        with gr.Column():
            pdf_input = gr.File(
                label="Upload PDF Manual",
                file_types=[".pdf"],
                type="filepath"
            )
            extract_btn = gr.Button("Extract Specifications", variant="primary")

        with gr.Column():
            output = gr.Dataframe(
                label="Extracted Specifications",
                headers=["Specification", "Value"],
                interactive=False,
                wrap=True,
            )

    extract_btn.click(
        fn=extract_specifications,
        inputs=pdf_input,
        outputs=output
    )


if __name__ == "__main__":
    MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3.2")
    host = os.getenv("GRADIO_HOST", "0.0.0.0")
    port = int(os.getenv("GRADIO_PORT", "7860"))

    EXTRACTOR = TechnicalSpecificationExtractor(
        model_name=MODEL_NAME,
        if_use_api=False,
        api_url=None,
        base_url=None,
    )

    demo.launch(server_name=host, server_port=port)
