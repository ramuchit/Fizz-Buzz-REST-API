from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

from validation_rules import FizzBuzzSchema
from query import generate_fizz_buzz_string

#load the env
load_dotenv()

# initialize the App
app = Flask(__name__)

#Enabled cors
cors = CORS(app, resourse={r"/api/*":{"origin":"*"}})

#initilize hit count dict
hit_counts = {}

@app.route('/api/fizz-buzz',methods=['POST'])
def fizz_buzz() -> str:
	# increment the hit count for the '/api/fizz-buzz' endpoint
	hit_counts['/api/fizz-buzz'] = hit_counts.get('/api/fizz-buzz',0)+1

	body = request.get_json()
	# validate Payload Json
	errors = FizzBuzzSchema().validate(body)
	
	if errors:
		return str(errors),400

	body['int1'] = int(body.get('int1'))
	body['int2'] = int(body.get('int2'))
	body['limit'] = int(body.get('limit')) + 1

	return generate_fizz_buzz_string(**body),200



@app.route('/api/most-frequent')
def most_frequent():
	most_frequent_endpoint = max(hit_counts,key=hit_counts.get)
	return jsonify({'most_frequent_endpoint': most_frequent_endpoint,'hit_count': hit_counts[most_frequent_endpoint]}), 200



# run the app debug True for dev mode and False for prod mode
if __name__ == '__main__':
	app.run(host=os.environ.get('HOST'), port=os.environ.get('POSRT'),debug=os.environ.get('DEBUG'))
