from pydantic import BaseModel, Field


class OllamaConfig(BaseModel):
    model_name: str = Field(
        description="Name of the Ollama model to use (e.g., 'llama2', 'mistral')"
    )
    if_use_api: bool = Field(
        default=False,
        description="Whether to use API endpoint instead of local Ollama instance"
    )
    api_url: str | None = Field(
        default=None,
        description="API URL endpoint when if_use_api is True"
    )
    base_url: str | None = Field(
        default="http://localhost:11434",
        description="Base URL for local Ollama instance (default: http://localhost:11434)"
    )
    
    def get_ollama_url(self) -> str:
        """Get the appropriate Ollama URL based on configuration."""
        if self.if_use_api and self.api_url:
            return self.api_url
        return self.base_url or "http://localhost:11434"

