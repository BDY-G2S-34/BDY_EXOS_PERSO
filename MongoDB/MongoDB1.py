import pymongo
from pymongo import MongoClient
client = MongoClient()

ENDPOINT = "34.244.43.135:27017"
USERNAME = "admin"
PASSWORD = "34.244.43.135:27017"

client = MongoClient(f'mongodb://{USERNAME}:{PASSWORD}@{ENDPOINT}/?directConnection=true')

client.list_database_names ()

