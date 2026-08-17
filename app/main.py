from typing import Annotated
import uvicorn
from fastapi import FastAPI, Query, HTTPException, Depends
from services.weather_api import get_weather
from schemas.models import WeatherResponse
from fastapi_limiter.depends import RateLimiter
from pyrate_limiter import Duration, Limiter, Rate

app = FastAPI()

@app.get(
    "/weather",
    response_model=WeatherResponse,
    dependencies=[Depends(RateLimiter(limiter=Limiter(Rate(5, Duration.SECOND * 10))))],
)

async def weather_endpoint(city: Annotated[str | None, Query(max_length=50)] = None):
    if city in [None, ""]:
        raise HTTPException(
            status_code=404,
            detail="city parameter is required",
        )
    result = get_weather(city)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1" ,port=8000,reload=True)