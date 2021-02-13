from flask import Flask
from rasa_nlu.model import Interpreter

interpreter = Interpreter.load("models/nlu/default/banknlu")
#result = interpreter.parse("Hey what'up?")

application = Flask(__name__)

@application.route('/')
def hello_world():    
    return 'Hello, World!'

@application.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User '+ str(username)
