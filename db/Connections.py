from configs.config import MONGO_CONNECTION_STRING, MONGO_DB_NAME
from pymongo import MongoClient


class Connection():
    client = MongoClient(MONGO_CONNECTION_STRING)
    db = client[MONGO_DB_NAME]

