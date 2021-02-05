from flask import Flask 

app = Flask(__name__)

#define starting point aka the root; forward slash is the highest level of 
# of hierarchy 
@app.route('/')
def hello_world():
    return 'Hello world'