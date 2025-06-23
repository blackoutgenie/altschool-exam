from pydantic import BaseModel

from schemas.registration import Registration


class RegistrationBase(BaseModel):
    id: str

    class Speaker(Registration):
        name: str
        topic: str