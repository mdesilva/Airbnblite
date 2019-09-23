from Controllers.Controller import Controller
from Services.PropertyService import PropertyService
from flask import Response, jsonify
from bson.objectid import ObjectId

class PropertyController(Controller):
    
    def __init__(self):
        self.collectionName = "properties"
        self.service = PropertyService()
        Controller.__init__(self)

    def addNewProperty(self, request):
        if not self.service.isUserVendor(request['owner']) :
            return Response("User is not a vendor", status=400, content_type="text/html")
        propertyDoc = {
            "name": request['name'],
            "type": request['type'],
            "price": request['price'],
            "owner": request['owner'],
            "renter": ""
        }
        self.db.insert("properties", propertyDoc)
        return Response(status=200)
    
    def get(self, id):
        propertyDoc = self.db.findOne("properties", {"_id": id})
        return jsonify(propertyDoc)

    """
    To rent a property, POST request will contain the 
    id of the property,
    username of the renter
    """
    def rentProperty(self, request):
        propertyId = request['propertyId']
        renter = request['renter']
        self.db.update("properties", {'_id': ObjectId(propertyId)}, {'$set': {"renter": renter}})
        return Response(status=200)
    
    def getAllAvailableProperties(self):
        properties = self.db.findMany("properties", {'renter': ""})
        return jsonify(properties)

    def getVendorProperties(self, owner):
        userProperties = self.db.findMany("properties", {'owner': owner})
        return jsonify(userProperties)

    def getRenterProperties(self, renter):
        rentedPropertiesByUser = self.db.findMany("properties", {'renter': renter})
        return jsonify(rentedPropertiesByUser)