import pymongo
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

client = MongoClient()

#ENDPOINT = "34.244.43.135:27017"
#USERNAME = "admin"
#PASSWORD = "34.244.43.135:27017"

#client = MongoClient(f'mongodb://{USERNAME}:{PASSWORD}@{ENDPOINT}/?directConnection=true')
#client = MongoClient(f'mongodb://localhost:27017')
client = MongoClient(host="localhost", port=27017)
#print(client.list_database_names ())
db = client['school_data']
"""
student = {
    "first_name": "Ashley",
    "last_name": "Jenkins",
    "dob": "2003-01-08T00:00:00Z",
    "grade_level": 8
}

result = db.students.insert_one(student)
print("ID du premier étudiant : {}".format(result.inserted_id))
"""

#db.list_collection_names()

"""
student1 = {
    "first_name": "Brian",
    "last_name": "McMantis",
    "dob": "2010-09-18T00:00:00Z",
    "grade_level": 2
}

student2 = {
    "first_name": "Leah",
    "last_name": "Drake",
    "dob": "2009-10-03T00:00:00Z",
    "grade_level": 2
}

new_students = db.students.insert_many([student1, student2])
print("Les ID des nouveaux étudiants sont : {}".format(new_students.inserted_ids))
"""
# print(db.students.find_one())

"""
list_students = db.students.find().sort('first_name',1)
for prenom in list_students:
    pprint(prenom)

query = {"first_name": "Brian"}
new_firstname = {
    "$set": {
        "first_name": "John"
    }
}
updated_students = db.students.update_one(query, new_firstname)
"""

#list_students = db.students.find().sort('first_name',1)
#for prenom in list_students:
#    pprint(prenom)

# Créer une collection
teachers = db.teachers

# Créer un document
teacher = {
    "first_name": "Sammy",
    "last_name": "White",
    "subject": ["Maths", "French", "English"],
    "classes": [8, 5, 2, 1]
}

# Insérer le document dans la collection
#result = teachers.insert_one(teacher)

"""
query = {"first_name" : "Sammy"}

updated_teachers = teachers.update_many(
    query,
    {
        "$set": {
            "classes.$[element]": 2
        }
    }, 
    array_filters=[{"element": {"$gte": 4}}]
)

print(updated_teachers.modified_count, "teacher mis à jour.")
"""

cursor = db.students.find()

entries = list(test)

print('Liste')
for y in entries:
    print(y)
    print()


df = pd.DataFrame(entries)
print('DataFrame')
print(df.head())