from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool38502"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """Shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)
