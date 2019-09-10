from database import DatabaseConnection
from flask import jsonify
class Property(object):

    def __init__(self):
        self.db = DatabaseConnection()

    def save(self):
        document = {
            "name": self.name,
            "type": self.type,
            "price": self.price
        }
        self.db.insert("properties", document)

    def create(self, name, propertyType, price):
        self.name = name
        self.type = propertyType
        self.price = price
    
    @staticmethod
    def get(self, id):
        return self.db.findOne("properties", {"_id": id})
