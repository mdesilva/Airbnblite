from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from database import DatabaseConnection
from bson.objectid import ObjectId
from SessionService import SessionService
from UserController import UserController
from PropertyController import PropertyController

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'airbnblite'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/airbnblite'

mongo = PyMongo(app)
db = DatabaseConnection()

UserController = UserController()
PropertyController = PropertyController()
SessionService = SessionService()

@app.route('/user/signup', methods=['POST'])
def signupUser():
    return UserController.signup(request.form)

@app.route('/user/login', methods=['POST'])
def loginUser():
    return UserController.login(request.form)

# Authenticated Routes
@app.route('/properties/<string:id>', methods=['GET'])
def getById(id):
    #An ObjectId is not the same as its string representation
    return PropertyController.get(ObjectId(id))

@app.route('/properties', methods=['GET'])
def getAll():
    return PropertyController.getAllAvailableProperties()

@app.route('/properties', methods=['POST'])
def addNewProperty():
    return PropertyController.addNewProperty(request.form)

@app.route('/properties/rent', methods=['POST'])
def rentProperty():
    return PropertyController.rentProperty(request.form)

@app.route('/theRequestIs', methods=['GET', 'POST'])
@SessionService.isUserLoggedIn()
def theRequestIs():
    return Response("Take a look at the server", content_type="text/html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)