from fastapi import APIRouter
from api.versions.v1 import router as v1_router

router = APIRouter()

@router.get("/", response_description="Api Version Manager route")
# Define the API Version Manager Route
async def hello_world():
    return {
        "location" : "api/",
        "message" : "Hello World",
        "version" : "1.0.0",
        "status" : 200,
        "status_message" : "OK",
        "data" : {
            "message" : "Welcome to the API"
        }
    }
    
router.include_router(v1_router, prefix="/v1", tags=["API Version 1"])
    
# Your API Updates Goes Here...
router.include_router(v1_router, prefix="/v2", tags=["API Version 2"])