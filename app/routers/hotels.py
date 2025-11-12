from fastapi import APIRouter, HTTPException, status

from app.data.hotel_repo import HotelRepo
from app.models.hotel import (
    HotelRequest,
    PartialHotelRequest,
    HotelResponse,
    HotelsResponse,
)


router = APIRouter(prefix="/hotels")
HOTEL_ID = "/{hotel_id}"

repo = HotelRepo()


def hotel_not_found(id: int):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Hotel with ID {id} not found"
    )


@router.get("")
def get_all_hotels() -> HotelsResponse:
    hotels = repo.get_all()
    return HotelsResponse(data=hotels)


@router.get(HOTEL_ID)
def get_hotel(hotel_id: int) -> HotelResponse:
    hotel = repo.get_by_id(hotel_id)

    if not hotel:
        raise hotel_not_found(hotel_id)

    return HotelResponse(data=hotel)


@router.post("", status_code=status.HTTP_201_CREATED)
def add_hotel(hotel: HotelRequest) -> HotelResponse:
    return HotelResponse(data=repo.add(hotel))


@router.put(HOTEL_ID)
def update_hotel(hotel_id: int, hotel: HotelRequest) -> HotelResponse:
    if not repo.exists_by_id(hotel_id):
        raise hotel_not_found(hotel_id)

    return HotelResponse(data=repo.update_by_id(hotel_id, hotel))


@router.patch(HOTEL_ID)
def patch_hotel(hotel_id: int, partialHotel: PartialHotelRequest) -> HotelResponse:
    if not repo.exists_by_id(hotel_id):
        raise hotel_not_found(hotel_id)

    return HotelResponse(data=repo.patch_by_id(hotel_id, partialHotel))


@router.delete(HOTEL_ID, status_code=status.HTTP_204_NO_CONTENT)
def delete_hotel(hotel_id: int) -> None:
    if not repo.exists_by_id(hotel_id):
        raise hotel_not_found(hotel_id)

    repo.delete_by_id(hotel_id)
