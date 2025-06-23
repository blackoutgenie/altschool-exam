from fastapi import HTTPException, status
import uuid
from app.models import User
from app.database import users
from app.schemas.user import UserCreate


class UserService:
    @staticmethod
    def create_user(user_data: UserCreate):
        user_id = str(uuid.uuid4())
        new_user = User(
            id=user_id,
            name=user_data.name,
            email=user_data.email
        )
        users[user_id] = new_user
        return new_user
    
    @staticmethod
    def get_user(user_id: str):
        if user_id not in users:
            return None
        return users[user_id]
    
    @staticmethod
    def get_all_users():
        return list(users.values())
    
    @staticmethod
    def update_user(user_id: str, user_data: UserCreate):
        if user-id not in users:
            raise HTTPException(status_code=404, detail="User not found")
        user = users[user_id]
        user.name = user_data.name
        user.email = user_data.email
        return {"Message": "User updated successfully"}
    
    @staticmethod
    def delete_user(user_id: str):
        if user_id not in users:
            raise HTTPException(status_code=404, detail="User not found")
        del users[user_id]
        return {"Message": "User deleted successfully"}
    
    @staticmethod
    def deactivate_user(user_id: str):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = False
        return user
    
user_service = UserService()