from flask import request, jsonify, Blueprint

blueprintHome = Blueprint('homeMethod', __name__)

@blueprintHome.route('/')
def query_records():
    return "Hello from the home page!"