from pydantic import BaseModel

class Role(BaseModel):
    id: int
    name: str
    permissions: list[str]
