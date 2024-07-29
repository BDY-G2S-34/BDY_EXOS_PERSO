# On télécharge un fichier de données
#!wget -q \
#    https://blent-learning-user-ressources.s3.eu-west-3.amazonaws.com/training/mongodb/data/country-by-languages.json \
#    -O /tmp/country-by-languages.json
import json
import pandas as pd
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient()

client = MongoClient(host="localhost", port=27017)

#print(client.list_database_names())

db = client['school_data']

"""


with open("D:/Bruno/Programmation/Data/Langues_Pays/country-by-languages.json", "r") as file:
    file_data = json.load(file)
    
Langues = db.Langues_Pays

if isinstance(file_data, list):
    Langues.insert_many(file_data) 
else:
    Langues.insert_one(file_data)
"""
"""
cursor = db.Langues_Pays.find()
entries = list(cursor)
df = pd.DataFrame(entries)
print(df.head())
"""
"""
result = db.students.delete_one({"_id": ObjectId('66a3b9ef97953e2295393cf8')})
print(result.acknowledged)
"""
result = db.students.delete_many({"_id": {"$ne": ObjectId('66a3bdffc3a3fb1b2198b244')}})
print(result.acknowledged)

db.students.drop()
