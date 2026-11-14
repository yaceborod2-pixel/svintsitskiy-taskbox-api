from fastapi import APIRouter, HTTPException, status
from database import User

router = APIRouter(
    prefix="/users",
    tags="Users"
)

@router.get("/users")
def get_users():
    users = User.get_users()

    return {
        "users" : users
    }

@router.get("/users/{user_id}")
def get_user(user_id: int):
    users = User.get_users()

    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    

    return 

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    
    users.pop(user_id)

    return status.HTTP_204_NO_CONTENT
