from flask import Flask
from flask_restful import Resource, Api
from AMEEparser import parseQuestion
import json
import random

app = Flask(__name__)
api = Api(app) 

questions = {'Haematology': [10935023, 10935032, 10940477, 10941038]}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class QuestionGetter(Resource):
	def get(self, category):
		
		questionQueue = list()
		for currQ in questions[category]:
			key = str(currQ)
			questionQueue.append(parseQuestion(key))
		
		return json.dumps({'category': category, 'questions': questionQueue})

api.add_resource(HelloWorld, '/')
api.add_resource(QuestionGetter, '/question/<string:category>')

if __name__ == '__main__':
    app.run(debug=True)