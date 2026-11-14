from fastapi import APIRouter, HTTPException, status
from app.database import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users():
    users = User.get_users()

    return {
        "users" : users
    }

@router.get("/{user_id}")
def get_user(user_id: int):
    user = User.get_user(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.delete("/{user_id}")
def delete_user(user_id: int):
    is_successfully = User.delete_user_by_id(user_id)
    
    if not is_successfully:
        raise HTTPException(status_code=404, detail="User not found")
    
    return status.HTTP_204_NO_CONTENT
