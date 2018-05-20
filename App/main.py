from flask import Flask, request, render_template
from flask_pymongo import PyMongo
from Scripts import bs4_Scrape_LOL

app = Flask("Scrape")
app.config['TEMPLATES_AUTO_RELOAD'] = True
mongo = PyMongo(app)


#Home Page
@app.route('/')
def home(data=bs4_Scrape_LOL.grab_data()):
    return render_template("home.html", n=1, data=data)
