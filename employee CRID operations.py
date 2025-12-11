from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["Employee"]            
collection = db["Employee"]

users = [{id: 1, "name": "Alice", "age": 30},
         {id: 2, "name": "Bob", "age": 25},     
         
         {id: 3, "name": "Charlie", "age": 35}]

collection.insert_many(users)   
print("Data inserted successfully.")    