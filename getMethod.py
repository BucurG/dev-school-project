from flask import request, jsonify, Blueprint
import json
from DataManager import DataManager

blueprintGet = Blueprint('GetMethod', __name__)


@blueprintGet.route('/')
def query_records():
    _id = request.args.get("id")
    return DataManager.sharedInstance().get(_id)
