from flask import Flask
from flask_restful import Api

## here is where you define your blueprint classes
from homeMethod import blueprintHome

## initialize the api
app = Flask(__name__)
api = Api(app)

## define host and port
api_rest_host = "0.0.0.0"
api_rest_port = 5001

## register your routes -> here we have the default page and 
##          we will create another class together
app.register_blueprint(blueprintHome, url_prefix='/')

## run your app
app.run(host=api_rest_host, port=api_rest_port, debug=True)