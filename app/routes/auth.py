from fastapi import APIRouter, HTTPException
from app.models.auth import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login", response_model=LoginResponse, summary="Login user")
def login(login_request: LoginRequest):
    if login_request.email == "test@example.com" and login_request.password == "password":
        return LoginResponse(token="jwt_token", token_type="Bearer")
    raise HTTPException(status_code=401, detail="Invalid credentials")
