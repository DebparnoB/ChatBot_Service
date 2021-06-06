from flask import Flask, make_response
from flask_cors import CORS, cross_origin
from rasa_nlu.model import Interpreter

interpreter = Interpreter.load("./models/nlu/default/current")

application = Flask(__name__)
CORS(application)

@application.route('/')
def hello_world():    
    return 'Hello, World!'

@application.route('/pred_intent/<user_text>')
def show_user_profile(user_text):
    # show the user profile for that user
    result = interpreter.parse(user_text
    return result["intent"]["name"]

@application.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User '+ str(username)
    
if(__name__=='__main__'):
    from waitress import serve
    serve(application, host='0.0.0.0, port=8000)
