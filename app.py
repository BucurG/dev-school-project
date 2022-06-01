from flask import Flask
from flask_restful import Api
from getMethod import blueprintGet
from postMethod import blueprintPost
from putMethod import blueprintPut
from deleteMethod import blueprintDelete

# here is where you define your blueprint classes
from homeMethod import blueprintHome

# initialize the api
app = Flask(__name__)
api = Api(app)

# define host and port
api_rest_host = "0.0.0.0"
api_rest_port = 5001

# register your routes -> here we have the default page and
# we will create another class together
app.register_blueprint(blueprintHome, url_prefix='/')
app.register_blueprint(blueprintGet, url_prefix='/get')
app.register_blueprint(blueprintPost, url_prefix='/post')
app.register_blueprint(blueprintPut, url_prefix='/put')
app.register_blueprint(blueprintDelete, url_prefix='/delete')

# run your app
app.run(host=api_rest_host, port=api_rest_port, debug=True)
