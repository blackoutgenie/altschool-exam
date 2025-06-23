from fastapi import HTTPException, status
import uuid
from app.models import Event
from app.database import events
from app.schemas.event import EventCreate


class EventService:
    @staticmethod
    def create_event(event_data: EventCreate):
        event_id = str(uuid.uuid4())
        new_event = Event(
            id = event_id,
            title = event_data.title,
            location = event_data.location,
            date = event_data.date
        )
        events[event_id] = new_event
        return new_event

    @staticmethod
    def get_event_by_id(event_id: str):
        if event_id not in events:
            return None
        return events[event_id]

    @staticmethod
    def get_all_events():
        return list(events.values())

    @staticmethod
    def update_event(event_id: str, event_data: EventCreate):
        if event_id not in events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        event = events[event_id]
        event.title = event_data.title
        event.location = event_data.location
        event.date = event_data.date
        return {"Message" : "Event updated successfully"}

    @staticmethod
    def delete_event(event_id: str):
        if event_id not in events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        del events[event_id]
        return {"message": "Event deleted successfully"}

    @staticmethod
    def close_event_registration(event_id: str):
        event = events.get(event_id)
        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        event.is_open = False
        return event




event_service = EventService()
