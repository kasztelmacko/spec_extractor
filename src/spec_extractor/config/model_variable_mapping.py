"""Mapping of SolarPanelSpecs field names to their display names and units."""

MODEL_VARIABLE_MAPPING: dict[str, dict[str, str]] = {
    "model_name": {
        "DisplayName": "Model Name",
        "Unit": "",
    },
    "height_mm": {
        "DisplayName": "Height",
        "Unit": "mm",
    },
    "width_mm": {
        "DisplayName": "Width",
        "Unit": "mm",
    },
    "depth_mm": {
        "DisplayName": "Depth/Thickness",
        "Unit": "mm",
    },
    "weight_kg": {
        "DisplayName": "Weight",
        "Unit": "kg",
    },
    "cable_length_mm": {
        "DisplayName": "Cable Length",
        "Unit": "mm",
    },
    "rated_power_w": {
        "DisplayName": "Rated Power",
        "Unit": "W",
    },
    "efficiency_pct": {
        "DisplayName": "Efficiency",
        "Unit": "%",
    },
    "nominal_voltage_v": {
        "DisplayName": "Nominal Voltage (Vmp)",
        "Unit": "V",
    },
    "max_voltage_v": {
        "DisplayName": "Max Voltage (Voc)",
        "Unit": "V",
    },
    "operational_amperage_a": {
        "DisplayName": "Operational Amperage (Imp)",
        "Unit": "A",
    },
    "min_operating_temperature": {
        "DisplayName": "Min Operating Temperature",
        "Unit": "°C",
    },
    "max_operating_temperature": {
        "DisplayName": "Max Operating Temperature",
        "Unit": "°C",
    },
    "wind_load_pa": {
        "DisplayName": "Max Wind Load",
        "Unit": "Pa",
    },
    "max_humidity_pct": {
        "DisplayName": "Max Humidity",
        "Unit": "%",
    },
    "cell_type": {
        "DisplayName": "Cell Type",
        "Unit": "",
    },
    "frame_material": {
        "DisplayName": "Frame Material",
        "Unit": "",
    },
    "connector_type": {
        "DisplayName": "Connector Type",
        "Unit": "",
    },
    "fire_rating": {
        "DisplayName": "Fire Rating",
        "Unit": "",
    },
}

