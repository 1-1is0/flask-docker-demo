import os
from flask import Flask
from pymongo import MongoClient
import json
import pymongo

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
	return "Hello people World!\n"


@app.route('/set/<name>')
def hello_name(name):
	name_id = add_name_to_db(name)
	return f"Hello {name}!\nyour id is {name_id}\n"


@app.route('/get')
def get_name():
	all_names = get_names()
	return json.dumps(list(all_names), indent=2)

def add_name_to_db(name):
	db = get_mongo_db()
	return db.names.insert_one({"name": name}).inserted_id

def get_names():
	db = get_mongo_db()
	return db.names.find({}, {"_id": 0})

def get_mongo_db():
	username = os.environ['MONGO_USER']
	passoword = os.environ["MONGO_PASSWORD"]
	mongo_db_url = f"mongodb://{username}:{passoword}@mongodb:27017"
	client = pymongo.MongoClient(mongo_db_url)
	return client.users

if __name__ == '__main__':
	app.run(host="0.0.0.0")
import os
from flask import Flask
from pymongo import MongoClient
import json
import pymongo

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
	return "Hello people World!\n"


@app.route('/set/<name>')
def hello_name(name):
	name_id = add_name_to_db(name)
	return f"Hello {name}!\nyour id is {name_id}\n"


@app.route('/get')
def get_name():
	all_names = get_names()
	return json.dumps(list(all_names), indent=2)

def add_name_to_db(name):
	db = get_mongo_db()
	return db.names.insert_one({"name": name}).inserted_id

def get_names():
	db = get_mongo_db()
	return db.names.find({}, {"_id": 0})

def get_mongo_db():
	username = os.environ['MONGO_USER']
	passoword = os.environ["MONGO_PASSWORD"]
	mongo_db_url = f"mongodb://{username}:{passoword}@mongodb:27017"
	client = pymongo.MongoClient(mongo_db_url)
	return client.users

if __name__ == '__main__':
	app.run(host="0.0.0.0")
