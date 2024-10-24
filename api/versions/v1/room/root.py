from fastapi import APIRouter
from api.models.Room import Room
import json

router = APIRouter()

@router.get("/", response_description="Api Version 1 Manager route")
async def hello_world():
    return {
        "location" : "api/v1/room",
        "message" : "API Version V1 - Initial Version",
        "version" : "1.0.0",
        "status" : 200,
        "status_message" : "OK... Working Version 1",
        "data" : {
            "message" : "Welcome to the API"
        }
    }
    
# Create Room Api 
# Description : Create a new room for Socket Server
# Request Type : POST
# Path : http://localhost:port/api/v1/room/create
# Default Port : 10007
@router.post("/create", response_description="Add New Room")
async def create_room(room: Room):
    try:
        Room.add_room(room.name, room.password)
        return {
            "status" : 200,
            "status_message" : "OK",
            "data" : {
                "message" : "Room Added Successfully"
            }
        }
    except ValueError as e:
        return {
            "status": 400,
            "status_message": "Bad Request",
            "data": {
                "message": str(e)
            }
        }
    except Exception as e:
        return {
            "status" : 500,
            "status_message" : "Internal Server Error",
            "data" : {
                "message" : str(e)
            }
        }
        
# Get All Rooms Api
# Description : Get All Rooms from the Database
# Request Type : GET
# Path : http://localhost:port/api/v1/room/list
# Default Port : 10007
@router.get("/list", response_description="Get All Rooms")
async def list_rooms():
    rooms = Room.get_rooms()
    rooms_json = [{"roomId": room["id"], "roomName": room["name"]} for room in rooms]

    return {
        "status" : 200,
        "status_message" : "OK",
        "data" : {
            "rooms" : rooms_json
        },
    }