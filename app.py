# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
import requests

import json

import operator

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

def parse_json(response_data):
	all_data = []
	for keys, values in response_data.items():
		temp_data = {}
		temp_data[keys] = values
		all_data.append(temp_data)
	return all_data

@app.route('/', methods=['GET'])
def get():
	url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
	payload = {}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	response_data = json.loads(response.text)['products']
	final_response = parse_json(response_data)
	return jsonify(final_response)


# driver function 
if __name__ == '__main__': 

	app.run(debug = True) 
