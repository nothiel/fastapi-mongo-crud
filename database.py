from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://root:MongoDB2019!@127.0.0.1:27017') 

class Database:
    def __init__(self) -> None:
        self.client = client       
        self.database = self.client['mentoriaric']
        self.users_collection = self.database['users']
    
    def create(self, values: dict) -> ObjectId:
        return self.users_collection.insert_one(values).inserted_id

    def read(self, id: ObjectId):
        return self.users_collection.find_one({'_id': id})

    def read_all(self):
        users = list(self.users_collection.find())
        for i in range(len(users)):
            users[i]['_id'] = str(users[i]['_id'])
        return users
    
    def update(self, id: ObjectId, update_data: dict):
        return self.users_collection.update_one({'_id': id}, {'$set': update_data})

    def delete(self, id: ObjectId):
        return self.users_collection.delete_one({'_id': id}).deleted_count