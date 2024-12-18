from fastapi import APIRouter, HTTPException
from app.models.user import User
from typing import List

router = APIRouter()

users = []

@router.get("/", response_model=List[User], summary="Fetch all users")
def get_users():
    return users

@router.post("/", response_model=User, summary="Create a user")
def create_user(user: User):
    if any(u.id == user.id for u in users):
        raise HTTPException(status_code=400, detail="User already exists")
    users.append(user)
    return user

@router.get("/{user_id}", response_model=User, summary="Fetch user by ID")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
