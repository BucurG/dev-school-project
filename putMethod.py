from flask import request, Blueprint
from DataManager import DataManager

blueprintPut = Blueprint('PutMethod', __name__)


@blueprintPut.route('/', methods=['PUT'])
def put_records():
    _id = int(request.args.get("id"))
    car = {
        "id": _id,
        "car_make": request.json["car_make"],
        "car_models": request.json["car_models"],
        "car_year": request.json["car_year"],
        "number_of_doors": request.json["number_of_doors"],
        "hp": request.json["hp"]
    }

    return DataManager.sharedInstance().update(_id, car)
