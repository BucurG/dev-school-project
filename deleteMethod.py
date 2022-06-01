from flask import request, Blueprint
from DataManager import DataManager

blueprintDelete = Blueprint('DeleteMethod', __name__)


@blueprintDelete.route('/', methods=['DELETE'])
def del_records():
    _id = request.args.get("id")
    return DataManager.sharedInstance().delete(_id)
