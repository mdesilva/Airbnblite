from Controller import Controller
from database import DatabaseConnection
from flask import Response
import hashlib #to encrypt and decrypt user passwords

class UserController(Controller):

    """
    Request to register new users will have their 
    first name,
    last name,
    email address as their username,
    password,
    account type (renter/vendor),
    """
    def signup(self, request):
        #assume that all fields have been submitted in the correct format
        #TODO: verify that all fields have been submitted in the correct format
        encryptedPassword = hashlib.sha256()
        encryptedPassword.update(request['password'].encode('UTF-8'))
        userDocument = {
            "firstName": request['firstName'],
            "lastName" : request['lastName'],
            "username": request['username'],
            "password": encryptedPassword.hexdigest(),
            "accountType": request['accountType']
        }
        self.db.insert("users", userDocument)
        print("User account created for " + userDocument['firstName'])
        return Response(status=200)