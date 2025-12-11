from pymongo import MongoClient     
client = MongoClient("mongodb://localhost:27017/")
db = client["Student"]
collection = db["StudentInfo"]

student = {"id" :1, "name": "John Doe", "age": 21, "Dept": "Computer Science"    }

collection.insert_one(student)
print("Student data inserted successfully.")