
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app) # wrap the app as an api

#create the resources
class Success(Resource):
    def get(self):
        return {'status': 'success'}


class Error(Resource):
    def get(self):
        1 / 0  # deliberatly raised error


#add resources to the app
api.add_resource(Success, '/success') #class and URI
api.add_resource(Error, '/error')

if __name__ == '__main__':
    app.run(debug=True)