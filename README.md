# Hotel API

Hotel booking system that provides CRUD operations for hotels and room availability checking.

## Project structure

```text
hotel-api
├── app/
│   ├── main.py        # Entry point
│   ├── data/          # In memory data
│   ├── models/        # Pydantic models
│   └── routers/       # Endpoints
├── README.md          # Documentation
└── requirements.txt   # Requirements
```

## Quick start

### Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate # windows: .venv\Scripts\activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn app.main:app --reload
```

> The API will be available at `http://localhost:8000`

## API Endpoints

### Health

#### `GET /health` check health

##### Response `200 OK`

```json
{
  "health": "OK"
}
```

### Hotels

#### `GET /hotels` returns all hotels

##### Response `200 OK`

```json
{
  "data": [
    {
      "id": 1,
      "name": "Grand Palace",
      "location": "Berlin",
      "rooms_available": 8,
      "price_per_night": 120.0
    },
    {
      "id": 2,
      "name": "Hilton",
      "location": "Cairo",
      "rooms_available": 17,
      "price_per_night": 106.0
    }
  ]
}
```

#### `GET /hotels/{hotel_id}` returns specific hotel

##### Response `200 OK`

```json
{
  "data": {
    "id": 1,
    "name": "Grand Palace",
    "location": "Berlin",
    "rooms_available": 8,
    "price_per_night": 120.0
  }
}
```

#### `POST /hotels` create new hotel

##### Request Body

```json
{
  "name": "New Hotel",
  "location": "Paris",
  "rooms_available": 25,
  "price_per_night": 150.0
}
```

##### Response `201 Created`

```json
{
  "data": {
    "id": 4,
    "name": "New Hotel",
    "location": "Paris",
    "rooms_available": 25,
    "price_per_night": 150.0
  }
}
```

#### `PUT /hotels/{hotel_id}` update entire hotel

##### Request Body

```json
{
  "name": "Updated Hotel",
  "location": "London",
  "rooms_available": 30,
  "price_per_night": 200.0
}
```

##### Response `200 OK`

```json
{
  "data": {
    "id": 1,
    "name": "Updated Hotel",
    "location": "London",
    "rooms_available": 30,
    "price_per_night": 200.0
  }
}
```

#### `PATCH /hotels/{hotel_id}` update hotel fields

##### Request Body

```json
{
  "rooms_available": 5
}
```

##### Response `200 OK`

```json
{
  "data": {
    "id": 1,
    "name": "Grand Palace",
    "location": "Berlin",
    "rooms_available": 5,
    "price_per_night": 120.0
  }
}
```

#### `DELETE /hotels/{hotel_id}` delete hotel

##### Response `204 No Content`

### Availability

#### `GET /availability` check room availability

##### Query Parameters

- `location` (optional): hotel's location
- `hotel` (optional): hotel's name

##### Examples

**Get all available hotels:**

```
GET /availability
```

**Filter by location:**

```
GET /availability?location=berlin
```

**Filter by hotel name:**

```
GET /availability?hotel=hilton
```

**Filter by both location and name:**

```
GET /availability?location=berlin&hotel=hilton
```

##### Response `200 OK`

```json
{
  "data": [
    {
      "id": 1,
      "name": "Grand Palace",
      "location": "Berlin",
      "rooms_available": 8,
      "price_per_night": 120.0
    },
    {
      "id": 3,
      "name": "Hilton",
      "location": "Berlin",
      "rooms_available": 12,
      "price_per_night": 124.0
    }
  ]
}
```

## Error Responses

### Hotel Not Found

Returned when attempting to access, update, or delete a hotel that doesn't exist.

#### Response `404 Not Found`

```json
{
  "detail": "Hotel with ID 99 not found"
}
```

### Validation Errors

Returned when request data is invalid.

#### Response `422 Unprocessable Entity`

```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": ["body", "rooms_available"],
      "msg": "Input should be greater than or equal to 0"
    }
  ]
}
```
