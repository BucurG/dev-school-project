from flask import request, Blueprint
from DataManager import DataManager

blueprintPost = Blueprint('PostMethod', __name__)


@blueprintPost.route('/', methods=['POST'])
def upload_records():
    car = {
        "car_make": request.json["car_make"],
        "car_models": request.json["car_models"],
        "car_year": request.json["car_year"],
        "number_of_doors": request.json["number_of_doors"],
        "hp": request.json["hp"]
    }

    DataManager.sharedInstance().post(car)
    return "Car saved successfuflly"
