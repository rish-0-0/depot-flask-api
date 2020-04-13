from functools import wraps
import json
import jwt
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

config = os.environ.get('SERVICE_ACCOUNT', None)
print(config)
config = json.loads(str(os.environ.get('SERVICE_ACCOUNT', None)).strip("'<>() ").replace('\'', '\"'))

def jsonFormat(key, value):
	return "\""+key+"\": "+"\""+value+"\""

with open('serviceAccount.json', 'w') as file:
	file.write('{\n')
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("type", config["type"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("project_id", config["project_id"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("private_key_id", config["private_key_id"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("private_key", config["private_key"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("client_email", config["client_email"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("client_id", config["client_id"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("auth_uri", config["auth_uri"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("token_uri", config["token_uri"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("auth_provider_x509_cert_url", config["auth_provider_x509_cert_url"]) + ",\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write(jsonFormat("client_x509_cert_url", config["client_x509_cert_url"]) + "\n")
with open('serviceAccount.json', 'a') as appender:
	appender.write("}")


print("SERVICE_ACCOUNT FILE MADE")
import firebase_methods

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['HS256_KEY']
CORS(app)


def needs_jwt(func):
	@wraps(func)
	def wrapped(*args, **kwargs):
		token = request.headers['X-AUTH-TOKEN']
		if not token:
			return jsonify({ 
				'success': False,
				'message': 'Missing Token'
			}), 401
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({ 'success': False, 'message' : 'Invalid Token'}), 403
		return func(*args, **kwargs)
	return wrapped

@app.route('/')
def run():
	return jsonify({
		'success': True,
		"message": "Welcome"
	})


@app.route('/api/v1/shops', methods=['GET'])
@needs_jwt
def get_shops():
	owner_id = request.args.get('owner_id')
	if not owner_id:
		return jsonify({
			success: False,
			message: "No owner_id was specified."
		})
	shops_of_owner = firebase_methods.get_shops(owner_id)
	jsonify({
		success: True,
		result: shops_of_owner
	})

@app.route('/api/v1/shops/upload', methods=['POST'])
def index():
    response = ""
    json_response = ""

    # Get the json from the request

    req = request.get_json()

    # Get the command from the json
    action = req.get('command')

    if action == 'add-excel':
        response = firebase_methods.add_excel(req.get('params'))
        json_response = jsonify(response)

    return json_response
	# test("MyShop")
	# return "Welcome to depot-flask-api."


if __name__ == '__main__':
	app.run()