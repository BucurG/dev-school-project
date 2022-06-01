from flask import request, Blueprint

blueprintPut = Blueprint('PutMethod', __name__)


@blueprintPut.route('/', methods=['PUT'])
def put_records():
    json = request.json
    return json
