from datetime import date
from pydantic import BaseModel

class EventBase(BaseModel):
    title: str
    location: str
    date: date


class EventCreate(EventBase):
    pass

class Event(EventBase):
    id : str
    is_open: bool