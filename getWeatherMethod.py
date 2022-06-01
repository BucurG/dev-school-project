from flask import request, jsonify, Blueprint
from ExternalApiManager import ExternalApiManager

blueprintGetWeather = Blueprint('GetWeatherMethod', __name__)


@blueprintGetWeather.route('/')
def get_weather_method():
    _city_name = request.args.get("city_name")
    _measurement_unit = request.args.get("measurement_unit")

    # Check that city name is not empty
    if not _city_name:
        return "City name not valid"

    # Check that measurement unit is valid
    if _measurement_unit == "f" or _measurement_unit == "c":
        return ExternalApiManager().get_weather_for_city(cityName=_city_name, measurement_unit=_measurement_unit)

    # If the measurement unit is not valid return an error
    return "Measurement unit not valid. Please use f or c only."
