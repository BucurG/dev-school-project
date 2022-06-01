import requests


class ExternalApiManager(object):

    def __init__(self):
        # Setting the api key
        self.apiKey = "33c83f81102a44bc8a8185657220106"

    def get_weather_for_city(self, cityName, measurement_unit):
        weather_request = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={self.apiKey}&q={cityName}&aqi=no").json()

        weather_response = {
            "city": weather_request["location"]["name"],
            "temperature": weather_request["current"][f"temp_{measurement_unit}"]
        }
        return weather_response
