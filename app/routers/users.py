from fastapi import APIRouter, HTTPException, status


router = APIRouter(
    prefix="/users",
    tags="Users"
)

@router.get("/users")
def get_users():
    return {
        "users" : users
    }

@router.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "users": users
    }

@router.delete("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    
    users.pop(user_id)

    return status.HTTP_204_NO_CONTENT
