from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
myDB=client["School"]
studentTable=myDB["students"]