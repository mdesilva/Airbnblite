from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo
from database import DatabaseConnection
from bson.objectid import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'airbnblite'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/airbnblite'

mongo = PyMongo(app)

db = DatabaseConnection('airbnblite')

@app.route('/properties/<string:id>', methods=['GET'])
def getById(id):
    #An ObjectId is not the same as its string representation
    return db.findOne("properties",{"_id": ObjectId(id)})

@app.route('/properties', methods=['GET'])
def getAll():
    return db.findAll("properties")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
