from flask import request
from flask_restful import Resource
from schematics.models import Model
from schematics.types import StringType
from schematics.exceptions import ValidationError, DataError


class User(Model):
    username = StringType(required=True)
    password = StringType(required=True)


class RegisterUser(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        user = User(json_data)
        try:
            user.validate()
            return json_data
        except (ValidationError, DataError) as e:
            return e.to_primitive()
