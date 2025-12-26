from flask import Flask,render_template

news_items = {
    1: {'id': 1, 
        'title': 'COVID-19 update', 
        'body': 'This is a news on COVID-19'},
    2: {'id': 2, 
        'title': 'Facemasks found', 
        'body': 'Recent news on facemask production'},
    3: {'id': 3,
        'title':'Python 4', 
        'body':'Python 4 will be out soon.... this is FAKE'},
}

name = "slowwy"
time = "now"



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name=name,time=time,news_items=news_items.values())

