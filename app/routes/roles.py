from fastapi import APIRouter
from app.models.role import Role

router = APIRouter()

roles = []

@router.get("/", response_model=list[Role], summary="Fetch all roles")
def list_roles():
    return roles

@router.post("/", response_model=Role, summary="Create a role")
def create_role(role: Role):
    roles.append(role)
    return role
