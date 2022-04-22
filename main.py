# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import datetime
import wikipedia
import ai_helper as ai_helper
import requests, json , sys
import requests, json , sys

ai_helpers = ai_helper.AI_HELPER()

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/msg')
def responses(msg):
    req = request.args.get('msg')    
    ints, resp = ai_helpers.ai_response("who are you")
    return ints,resp

# main driver function
if __name__ == '__main__':
    
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug = True, port = 5000)