from database import DatabaseConnection
import hashlib 

class UserService():

    def __init__(self):
        self.db = DatabaseConnection()
        self.collection = "users"
    
    def isUser(self, username):
        if self.db.findOne(self.collection, {"username": username}):
            return True
        else:
            return False
    
    def authenticate(self, request):
        print(request)
        return True
        username = request['username']
        password = request['password']
        user = self.db.findOne(self.collection, {'username': username})
        encryptedPassword = hashlib.sha256()
        encryptedPassword.update(password.encode('UTF-8'))
        if (encryptedPassword.hexdigest() == user['password']):
            print("User " + username + " authenticated")
            return True
        else:
            print("User " + username +  " provided incorrect credentials")
            return False
        