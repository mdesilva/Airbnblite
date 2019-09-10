from pymongo import MongoClient
from flask import jsonify

class DatabaseConnection():

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client["airbnblite"]

    def findOne(self,collectionName,query):
        collection = self.db[collectionName]
        result = collection.find_one(query, {'_id':0})
        action = "Get for {}".format(collectionName)
        print(action)
        return result
    
    def findAll(self,collectionName):
        collection = self.db[collectionName]
        cursor = collection.find({},{'_id':0})
        result = []
        for row in cursor:
            result.append(row)
        action = "Get all documents for {}".format(collectionName)
        print(action)
        return jsonify(result)

    def insert(self,collectionName,document):
        action = "Inserting one document into {}".format(collectionName)
        print(action)
        self.db[collectionName].insert_one(document)
        return True