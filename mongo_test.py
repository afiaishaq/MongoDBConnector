from pymongo import MongoClient

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://afiaishaq_mlops:afiaishaq_mlops@cluster0.nps0gnd.mongodb.net/?retryWrites=true&w=majority")

# create database
db = client["mlops_db"]

# create collection
collection = db["students"]

# insert data
data = {
    "name": "Afia",
    "course": "MLOps",
    "platform": "MongoDB Atlas"
}

collection.insert_one(data)

print("MongoDB connected and data inserted successfully!")