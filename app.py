import json
import os

config = os.environ.get('SERVICE_ACCOUNT', None)
print(config)
config = json.loads(config)

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





from flask import Flask
from firebase_methods import test

app = Flask(__name__)

@app.route('/')
@app.route('/api')
def index():
	test("MyShop")
	return "Welcome to depot-flask-api."