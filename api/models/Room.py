from db import rooms_collection
from bson.objectid import ObjectId

class Room:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @staticmethod
    def add_room(name, password):
        """ Adds a new room to the collection. """
        try:
            if rooms_collection.find_one({'name': name}):
                raise Exception('Room already exists')
            rooms_collection.insert_one({'name': name, 'password': password})
        except Exception as e:
            raise e

    @staticmethod
    def get_rooms():
        """ Retrieves all rooms with their ids and names. """
        rooms = rooms_collection.find({}, {'name': 1})
        return [(str(room['_id']), room['name']) for room in rooms]

    @staticmethod
    def get_room_by_name(name):
        """ Retrieves a room by its name. """
        room = rooms_collection.find_one({'name': name})
        return room

    @staticmethod
    def get_room_by_id(room_id):
        """ Retrieves a room by its id. """
        if not ObjectId.is_valid(room_id):
            raise Exception('Invalid room ID')

        room = rooms_collection.find_one({'_id': ObjectId(room_id)})
        return room

    @staticmethod
    def delete_room(room_id):
        """ Deletes a room by its ID. """
        if not ObjectId.is_valid(room_id):
            raise Exception('Invalid room ID')

        result = rooms_collection.delete_one({'_id': ObjectId(room_id)})
        if result.deleted_count == 0:
            raise Exception('Room not found or already deleted')
        return result

