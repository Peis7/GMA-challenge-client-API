from flask import Flask,jsonify,request
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
import os
import json

load_dotenv('../.env') # take environment variables from .env.


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route("/v1/client/<id>")
def client_by(id):
    client =  mongo.db.clients.find_one({"clientId": id})
    return parse_json(client if client else {'message': 'No client found'}), 200

if __name__=="__main__":
    app.run(debug=os.getenv('DEBUG', False), host="0.0.0.0",port=os.getenv('APP_PORT'))