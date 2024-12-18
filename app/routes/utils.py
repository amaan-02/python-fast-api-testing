from fastapi import APIRouter

router = APIRouter()

@router.get("/info", summary="Fetch utility info")
def get_info():
    return {"info": "This is a utility endpoint"}
