from app import app
from flask_restful import Resource, Api

api = Api(app)

class ApiV10(Resource):
	def post(self):