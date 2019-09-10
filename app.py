from flask import Flask
from flask import jsonify
from flask import request, Response
from flask_pymongo import PyMongo
from database import DatabaseConnection
from bson.objectid import ObjectId
from property import Property
from UserController import UserController
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'airbnblite'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/airbnblite'

mongo = PyMongo(app)
db = DatabaseConnection()

UserController = UserController()
@app.route('/user/signup', methods=['POST'])
def signupUser():
    return UserController.signup(request.form)

@app.route('/user/login', methods=['POST'])
def loginUser():
    return UserController.login(request.form)

@app.route('/properties/<string:id>', methods=['GET'])
def getById(id):
    #An ObjectId is not the same as its string representation
    return Property.get(ObjectId(id))

@app.route('/properties', methods=['GET'])
def getAll():
    return db.findAll("properties")

@app.route('/properties', methods=['POST'])
def addNewProperty():
    print(request.form)
    newProperty = Property()
    newProperty.create(request.form['name'], request.form['type'], request.form['price'])
    newProperty.save()
    return Response(status=200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
