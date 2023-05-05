from flask import Flask
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import flask_restful import Api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///crud1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

from app.models.survivors import Survivors
with app.app_context(): #garantir que as tabelas existam
    db.create_all()


'''
@app.route("/")
def index():
    return "<h1> Aplicação Flask</h1>"
'''
