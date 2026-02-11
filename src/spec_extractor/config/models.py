from pydantic import BaseModel, Field

class SolarPanelSpecs(BaseModel):
    """Data model for solar panel technical specifications extracted from PDF manuals."""
    model_name: str = Field(description="The full product name from the header")

    height_mm: float | None = Field(default=None, description="Panel height in millimeters")
    width_mm: float | None = Field(default=None, description="Panel width in millimeters")
    depth_mm: float | None = Field(default=None, description="Panel depth/thickness in millimeters")
    weight_kg: float | None = Field(default=None, description="Panel weight in kilograms")
    cable_length_mm: float | None = Field(default=None, description="Length of attached cable in millimeters")

    rated_power_w: float = Field(description="Normalized power in Watts (Rated/Output/Nominal/Peak)")
    efficiency_pct: float | None = Field(default=None, description="Conversion efficiency percentage in %")
    nominal_voltage_v: float | None = Field(default=None, description="Vmp or Nominal Voltage in Volts")
    max_voltage_v: float | None = Field(default=None, description="Voc or Max System Voltage in Volts")
    operational_amperage_a: float | None = Field(default=None, description="Imp or operational amperage in Ampers")
    
    min_operating_temperature: float | None = Field(default=None, description="Minimum operating temperature in degrees Celsius")
    max_operating_temperature: float | None = Field(default=None, description="Maximum operating temperature in degrees Celsius")
    wind_load_pa: float | None = Field(default=None, description="Maximum wind load capacity in Pascals")
    max_humidity_pct: float | None = Field(default=None, description="Max operating humidity range in %")
    
    cell_type: str | None = Field(default=None, description="e.g., Mono-PERC")
    frame_material: str | None = Field(default=None, description="e.g., Aluminum")
    connector_type: str | None = Field(default=None, description="e.g., MC4")
    fire_rating: str | None = Field(default=None, description="Fire safety rating classification (e.g., Class A, Class C)")
