from pymongo import MongoClient
from bson.objectid import ObjectId

# Initialize MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['template']  # Database name

# Initialize the collection for rooms and devices
rooms_collection = db['rooms']
devices_collection = db['devices']
otp_collection = db['otps']   # Collection for OTPs

user_collection = db['users']   # Collection for users

