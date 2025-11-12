from fastapi import APIRouter


from app.data.hotel_repo import HotelRepo
from app.models.hotel import Hotel, HotelsResponse

router = APIRouter(prefix="/availability")
hotel_repo = HotelRepo()


@router.get("")
def availability(location: str = "", hotel: str = "") -> HotelsResponse:
    hotels: list[Hotel] = []

    if not location and not hotel:
        hotels = hotel_repo.get_available()

    elif location and hotel:
        hotels = hotel_repo.get_available_by_location_and_name(location, hotel)

    elif location:
        hotels = hotel_repo.get_available_by_location(location)

    elif hotel:
        hotels = hotel_repo.get_available_by_name(hotel)

    return HotelsResponse(data=hotels)
