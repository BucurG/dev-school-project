import json


class DataManager(object):

    _sharedInstance = None

    def __init__():
        raise RuntimeError("Cannot call init externally.")

    def load_json(self):
        with open('tmp/data.json', 'r') as file:
            self.__internalJson = json.load(file)

    def get(self, id):
        intId = int(id)
        for car in self.__internalJson:
            if car["id"] == intId:
                return car
        return "Car not found"

    def post(self, car):
        car["id"] = len(self.__internalJson)
        self.__internalJson.append(car)
        self.save_file()

    def delete(self, id):
        indexToPop = None
        for index, car in enumerate(self.__internalJson):
            if int(id) == car["id"]:
                indexToPop = index
                break

        if indexToPop:
            self.__internalJson.pop(index)
            self.save_file()
            return f"Deleted {id} successfuly"
        return f"Index {id} not found"

    def save_file(self):
        json.dump(self.__internalJson, open("tmp/data.json", "w"),
                  indent=3, separators=(',', ': '))
        print("Saved file successfly")

    @classmethod
    def sharedInstance(cls):
        global _sharedInstance
        if cls._sharedInstance is None:
            cls._sharedInstance = cls.__new__(cls)
            cls._sharedInstance.load_json()
            return cls._sharedInstance
        return cls._sharedInstance
