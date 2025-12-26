from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ""

@app.route('/hello/')
def hello_world1():
    return 'Hi my name is neck hurt vroooo'