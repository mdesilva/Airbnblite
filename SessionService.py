from database import DatabaseConnection

class SessionService():

    def __init__(self):
        self.db = DatabaseConnection()

    def isUserLoggedIn(self, func):
        def wrapper(*args, **kwargs):
            print("The request is ")
            print(args[0])
        return wrapper