from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import mysql.connector
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysql:\\root@password:localhost\FashionDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)

@app.route('/',methods = ['GET','POST'])
def test_insert():
    return "Hello"