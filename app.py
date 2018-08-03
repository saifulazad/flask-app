from flask import Flask
from flask_restful import Api

from resources import RegisterUser

app = Flask(__name__)
api = Api(app)

api.add_resource(RegisterUser, '/register')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
