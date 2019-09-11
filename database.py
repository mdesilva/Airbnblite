from pymongo import MongoClient
from flask import jsonify

class DatabaseConnection():

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client["airbnblite"]

    def appendToObject(self, cursor):
        result = []
        for row in cursor:
            result.append(row)
        return result

    def findOne(self, collectionName, query):
        collection = self.db[collectionName]
        result = collection.find_one(query, {'_id':0})
        action = "Get for {}".format(collectionName)
        print(action)
        return result
    
    def findMany(self, collectionName, query):
        collection = self.db[collectionName]
        cursor = collection.find(query, {'_id':0})
        result = self.appendToObject(cursor)
        return result

    def findAll(self,collectionName):
        action = "Get all documents for {}".format(collectionName)
        print(action)
        collection = self.db[collectionName]
        cursor = collection.find({},{'_id':0})
        result = self.appendToObject(cursor)
        return jsonify(result)

    def insert(self,collectionName,document):
        action = "Inserting one document into {}".format(collectionName)
        print(action)
        self.db[collectionName].insert_one(document)
        return True

    def update(self,collectionName,filter,query):
        self.db[collectionName].update_one(filter, query)
        return True