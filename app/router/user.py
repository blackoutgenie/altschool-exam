from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate
from app.services.user import user_service

user_router = APIRouter()


@user_router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    return user_service.create_user(user_data)


@user_router.get("/", status_code=status.HTTP_200_OK)
def get_all_user():
    return user_service.get_all_users()


@user_router.get("/user_id", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: str):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@user_router.put("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: str):
    return user_service.delete_user(user_id)

@user_router.patch("/{user_id}/deactivate", status_code=status.HTTP_200_OK)
def deactivate_user(user_id: str):
    return user_service.deactivate_user(user_id)