from fastapi import APIRouter, HTTPException, status
from app.schemas.event import EventCreate
from app.services.event import event_service

event_router = APIRouter()


@event_router.post("/", status_code=201)
def create_event(event_data: EventCreate):
    return event_service.create_event(event_data)

@event_router.get("/", status_code=status.HTTP_200_OK)
def get_all_events():
    return event_service.get_all_events()


@event_router.get("/{event_id}", status_code=200)
def get_event(event_id: str):
    event = event_service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return event

@event_router.put("/{event_id}", status_code=status.HTTP_201_CREATED)
def update_event(event_id: str, event_data: EventCreate):
    return event_service.update_event(event_id, event_data)

@event_router.delete("/{event_id}", status_code = status.HTTP_200_OK)
def delete_event(event_id: str):
    return event_service.delete_event(event_id)

@event_router.patch("/{event_id}", status_code=status.HTTP_200_OK)
def close_event_registration(event_id: str):
    closed = event_service.close_event_registration(event_id)
    if not closed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found or already closed")
    return closed