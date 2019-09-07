from database import DatabaseConnection
from flask import jsonify
class Property(object):

    def __init__(self, name, propertyType, price):
        self.name = name
        self.type = propertyType
        self.price = price
        self.db = DatabaseConnection("airbnblite")

    def save(self):
        document = {
            "name": self.name,
            "type": self.type,
            "price": self.price
        }
        self.db.insert("properties", document)
