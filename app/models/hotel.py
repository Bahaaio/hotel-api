from pydantic import BaseModel, NonNegativeFloat, NonNegativeInt


class Hotel(BaseModel):
    id: int
    name: str
    location: str
    rooms_available: NonNegativeInt
    price_per_night: NonNegativeFloat


class HotelRequest(BaseModel):
    name: str
    location: str
    rooms_available: NonNegativeInt
    price_per_night: NonNegativeFloat


class PartialHotelRequest(BaseModel):
    name: str | None = None
    location: str | None = None
    rooms_available: NonNegativeInt | None = None
    price_per_night: NonNegativeFloat | None = None


class HotelResponse(BaseModel):
    data: Hotel


class HotelsResponse(BaseModel):
    data: list[Hotel]
