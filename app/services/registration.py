from fastapi import HTTPException, status
from datetime import date
import uuid
from app.models import Registration
from app.database import registrations
from app.schemas.registration import RegistrationCreate
from app.services.event import event_service
from app.services.user import user_service


def user_registered_for_event(user_id: str, event_id: str) -> bool:
    return any(
        reg.user_id == user_id and reg.event_id == event_id
        for reg in registrations.values()
    )


class RegistrationService:
    @staticmethod
    def register_user(registration_data: RegistrationCreate):
        user =  user_service.get_user_by_id(registration_data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.is_active:
            raise HTTPException(status_code=400, detail="Inactive users cannot register")

        event = event_service.get_event_by_id(registration_data.event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if not event.is_open:
            raise HTTPException(status_code=400, detail="Event registration is closed")

        if user_registered_for_event(registration_data.user_id, registration_data.event_id):
            raise HTTPException(status_code=400, detail="User already registered for this event")

        registration_id = str(uuid.uuid4())
        new_registration = Registration(
            id=registration_id,
            user_id=registration_data.user_id,
            event_id=registration_data.event_id,
            registration_date=date.today()
        )
        registrations[registration_id] = new_registration
        return new_registration

    @staticmethod
    def mark_attendance(registration_id: str):
        if registration_id not in registrations:
            raise HTTPException(status_code=404, detail="Registration not found")
        registrations[registration_id].attended = True
        return registrations[registration_id]

    @staticmethod
    def get_user_registrations(registration_id: str):
        if registration_id not in registrations:
            raise HTTPException(status_code=404, detail="User not found")
        return registrations[registration_id]


registration_service = RegistrationService()
   