import os
from pymongo import MongoClient

PASSWORD = os.getenv('MONGO_PASSWORD')
assert PASSWORD, "MONGO_PASSWORD environment variable is not set!"
print(PASSWORD)

client = MongoClient(f'mongodb+srv://c8a:{PASSWORD}@cluster0.ow0ob.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.mytestdb
print(db.list_collection_names())