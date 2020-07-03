# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import lists
import random
from datetime import datetime
# from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# name of database
# app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri'

# mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    letter = random.choice(lists.letters)
    cats = random.choices(lists.categories, k=8)
    return render_template('index.html', categories=cats, letter=letter, time=datetime.now())


# CONNECT TO DB, ADD DATA

@app.route('/results')
def results():
    # connect to the database

    # insert new data

    # return a message to the user
    return ""


# TO DO LIST
# Make it look prettier
# Show a results pages with the results from other players too
# Or a "play against the computer" which has answers already
# Results submitted when timer runs out
# Show points from the game
# Make the game more customizable (num of categories, timer length, what letters)