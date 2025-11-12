from app.models.hotel import Hotel, HotelRequest, PartialHotelRequest


class HotelRepo:
    hotels: dict[int, Hotel] = {
        1: Hotel(
            id=1,
            name="Grand Palace",
            location="Berlin",
            rooms_available=8,
            price_per_night=120.0,
        ),
        2: Hotel(
            id=2,
            name="Hilton",
            location="Cairo",
            rooms_available=17,
            price_per_night=106.0,
        ),
        3: Hotel(
            id=3,
            name="Hilton",
            location="Berlin",
            rooms_available=12,
            price_per_night=124.0,
        ),
    }
    last_id: int = len(hotels)

    def get_new_id(self) -> int:
        self.last_id = self.last_id + 1

        return self.last_id

    def get_all(self) -> list[Hotel]:
        return list(self.hotels.values())

    def get_by_id(self, id: int) -> Hotel | None:
        return self.hotels.get(id)

    def get_available(self) -> list[Hotel]:
        return [hotel for hotel in self.hotels.values() if hotel.rooms_available > 0]

    def get_available_by_location(self, location: str) -> list[Hotel]:
        return [
            hotel
            for hotel in self.hotels.values()
            if hotel.rooms_available > 0
            and _matches_case_insensitive(hotel.location, location)
        ]

    def get_available_by_name(self, name: str) -> list[Hotel]:
        return [
            hotel
            for hotel in self.hotels.values()
            if hotel.rooms_available > 0 and _matches_case_insensitive(hotel.name, name)
        ]

    def get_available_by_location_and_name(
        self, location: str, name: str
    ) -> list[Hotel]:
        return [
            hotel
            for hotel in self.hotels.values()
            if hotel.rooms_available > 0
            and _matches_case_insensitive(hotel.location, location)
            and _matches_case_insensitive(hotel.name, name)
        ]

    def exists_by_id(self, id: int) -> bool:
        return id in self.hotels

    def add(self, hotelRequest: HotelRequest) -> Hotel:
        new_id = self.get_new_id()

        new_hotel = Hotel(id=new_id, **hotelRequest.model_dump())
        self.hotels[new_id] = new_hotel

        return new_hotel

    def update_by_id(self, id: int, hotelRequest: HotelRequest) -> Hotel:
        updated_hotel = Hotel(id=id, **hotelRequest.model_dump())
        self.hotels[id] = updated_hotel

        return updated_hotel

    def patch_by_id(self, id: int, partialHotel: PartialHotelRequest) -> Hotel:
        existing_hotel = self.hotels[id].model_dump()
        existing_hotel.update(partialHotel.model_dump(exclude_unset=True))

        updated_hotel = Hotel(**existing_hotel)
        self.hotels[id] = updated_hotel

        return updated_hotel

    def delete_by_id(self, id: int) -> None:
        self.hotels.pop(id)


def _matches_case_insensitive(a: str, b: str):
    return a.lower() == b.lower()
