from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    temp_max: float
    temp_min: float
    feels_like: float
    conditions: str
    