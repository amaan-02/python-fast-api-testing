from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health", summary="Check API health")
def health_check():
    return {"status": "healthy"}

@router.get("/time", summary="Fetch server time")
def server_time():
    return {"time": datetime.utcnow().isoformat()}
