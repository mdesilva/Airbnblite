import flask_login
from flask import Flask, jsonify, request, Response
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
from Controllers.UserController import UserController
from Controllers.PropertyController import PropertyController
from Services.UserService import UserService
from Models.User import User

app = Flask(__name__)
CORS(app)
app.secret_key = "air bnb lite"
app.config['MONGO_DBNAME'] = 'airbnblite'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/airbnblite'

mongo = PyMongo(app)

UserService = UserService()
User = User()
UserController = UserController()
PropertyController = PropertyController()
SessionService = LoginManager()
SessionService.init_app(app)

#Authentication setup
@SessionService.user_loader
def user_loader(username):
    if not UserService.isUser(username):
        return
    user = User
    user.id = username
    return user

@SessionService.request_loader
def request_loader(request):
    if not request.form:
        return
    if not UserService.authenticate(request.form):
        return
    user = User
    user.id = request.form["username"]
    user.is_authenticated = True
    return user

# User account Routes
@app.route('/user/signup', methods=['POST'])
def signupUser():
    return UserController.signup(request.form)

@app.route('/user/login', methods=['POST'])
def loginUser():
    print(request.form["data"])
    return Response(status=200)
    """
    if UserService.authenticate(request.form):
        user = User
        user.id = request.form["username"]
        flask_login.login_user(user)
        return Response(status=200)
    """

@app.route('/user/logout')
def logoutUser():
    if flask_login.current_user.id:
        flask_login.logout_user()
        return Response(status=200)
    else:
        return Response("No user currently logged in", content_type="text/html")

# Authenticated Routes
@app.route('/properties/id/<string:id>', methods=['GET'])
def getById(id):
    #An ObjectId is not the same as its string representation
    return PropertyController.get(ObjectId(id))

@app.route('/properties', methods=['GET'])
#@flask_login.login_required
def getAll():
    return PropertyController.getAllAvailableProperties()

@app.route('/properties/vendor/<string:username>', methods=['GET'])
#@flask_login.login_required
def getVendorProperties(username):
    return PropertyController.getVendorProperties(username)

@app.route('/properties/renter/<string:username>', methods=["GET"])
def getPropertiesRentedByUser(username):
    return PropertyController.getRenterProperties(username)

@app.route('/properties', methods=['POST'])
def addNewProperty():
    return PropertyController.addNewProperty(request.form)

@app.route('/properties/rent', methods=['POST'])
def rentProperty():
    return PropertyController.rentProperty(request.form)

@app.route('/protected', methods=['GET'])
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)