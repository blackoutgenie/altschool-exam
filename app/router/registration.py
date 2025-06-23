from fastapi import APIRouter, status
from app.services.registration import registration_service
from app.database import registrations
from app.schemas.registration import RegistrationCreate


registration_router = APIRouter()


@registration_router.post("/", status_code=status.HTTP_201_CREATED)
def register_user(registration_data: RegistrationCreate):
    return registration_service.register_user(registration_data)


@registration_router.patch("/{registration_id}/attend", status_code=status.HTTP_200_OK)
def mark_attendance(registration_id: str):
    return registration_service.mark_attendance(registration_id)

@registration_router.get("/{registration_id}", status_code=status.HTTP_200_OK)
def get_user_registration(registration_id: str):
    return registration_service.get_user_registration(registration_id)

@registration_router.get("/", status_code=status.HTTP_200_OK)
def get_all_registrations():
    return list(registrations.values())