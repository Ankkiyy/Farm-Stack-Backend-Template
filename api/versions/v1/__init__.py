from fastapi import APIRouter
from api.versions.v1.room.root import router as room_router

router = APIRouter()

@router.get("/", response_description="Api Version 1 Manager route")
async def hello_world():
    return {
        "location" : "api/v1",
        "message" : "API Version V1 - Initial Version",
        "version" : "1.0.0",
        "status" : 200,
        "status_message" : "OK... Working Version 1",
        "data" : {
            "message" : "Welcome to the API"
        }
    }

router.include_router(room_router, prefix="/room", tags=["API Version 1"])