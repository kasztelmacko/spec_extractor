"""Configuration module for spec extractor."""

from src.spec_extractor.config.models import SolarPanelSpecs
from src.spec_extractor.config.config import OllamaConfig
from src.spec_extractor.config.model_variable_mapping import MODEL_VARIABLE_MAPPING

__all__ = [
    "SolarPanelSpecs",
    "OllamaConfig",
    "MODEL_VARIABLE_MAPPING",
]

