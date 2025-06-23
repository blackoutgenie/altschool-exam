from pydantic import BaseModel
from datetime import date

class RegistrationBase(BaseModel):
    user_id : str
    event_id : str


class RegistrationCreate(RegistrationBase):
    pass


class Registration(RegistrationBase):
    id: str
    registration_date: date = date.today()
    attended : bool = False