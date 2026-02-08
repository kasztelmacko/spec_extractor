from pydantic import BaseModel, Field

class SolarSpecs(BaseModel):
    model_name: str = Field(description="The full product name from the header")
    rated_power_w: int = Field(description="Normalized power in Watts (Rated/Output/Nominal/Peak)")
    efficiency_pct: float | None = Field(default=None, description="Conversion efficiency percentage")
    
    nominal_voltage_v: float | None = Field(default=None, description="Vmp or Nominal Voltage")
    max_voltage_v: float | None = Field(default=None, description="Voc or Max System Voltage")
    current_a: float | None = Field(default=None, description="Imp or operational amperage")
    
    height_mm: float | None = Field(default=None)
    width_mm: float | None = Field(default=None)
    depth_mm: float | None = Field(default=None)
    weight_kg: float | None = Field(default=None)
    
    cell_type: str | None = Field(default=None, description="e.g., Mono-PERC")
    frame_material: str | None = Field(default=None, description="e.g., Aluminum")
    connector_type: str | None = Field(default=None, description="e.g., MC4")