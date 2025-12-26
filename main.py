from flask import Flask, render_template, request, redirect, url_for,render_template_string
from datetime import datetime

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
time = datetime.now()

def new_news_item(title, body):
    new_id = max(news_items.keys()) + 1
    return {
        'id': new_id,
        'title': title,
        'body': body
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name=name,time=time,news_items=news_items.values())


@app.route('/news/<id>/')
def show_news_item(id):
    news_item = news_items[int(id)]
    query = request.args.get('query', default="", type=str)
    temp = open("/home/vali/ku_web_jittat/templates/index.html", "r").read()
    return render_template_string(temp.replace("{query}",query),
                           id=news_item['id'],
                           title=news_item['title'],
                           body=news_item['body'])


@app.route('/news/create/',methods = ["POST"])
def create_news_item():
    title = request.form["title"]
    body = request.form["body"]
    print(f"Your tile: {title}, body: {body}")
    new_item = new_news_item(title,body)
    news_items[new_item["id"]] = new_item
    return redirect(url_for('index'))
