from flask import Flask 

app = Flask(__name__)

@app.route ("/")
def welcome ():
    return "welcom to my new page "
