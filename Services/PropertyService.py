from database import DatabaseConnection

class PropertyService():

    def __init__(self):
        self.db = DatabaseConnection()
        self.collection = "users"

    def isUserVendor(self, username):
        user = self.db.findOne(self.collection, {"username": username})
        if (user['accountType'] == 'vendor'):
            return True
        else:
            return False