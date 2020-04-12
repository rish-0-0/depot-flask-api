import json
import os

config = os.environ['SERVICE_ACCOUNT']
config = json.loads(config)

with open('serviceAccount.json', 'w') as file:
	file.write(json.dumps(config, indent=4, sort_keys=True))





from flask import Flask
from firebase_methods import test

app = Flask(__name__)

@app.route('/')
def index():
	test("MyShop")
	return "Welcome to depot-flask-api."