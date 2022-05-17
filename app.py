from lib2to3.pytree import Base
from flask import Flask
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# import mysql.connector
from flask_login import UserMixin
import pymysql

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:password@localhost/FashionDB')
SessionLocal = sessionmaker(bind = engine,autocommit = False)
session = SessionLocal()
Base = declarative_base(bind = engine)
# my_db = mysql.connector.connect(
#     host = "localhost"
#     name = "root"
#     passwd = "password"
# )

# my_cursor = my_db.cursor()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(Integer)

@app.route('/',methods = ['GET','POST'])
def test_insert():
    new_user = Users(name = "Vishal",password = "123456", email = "abc@aa",phone = 12345679)
    session.add(new_user)
    session.commit()
    return "data added"

if __name__ == '__main__':
    app.run(debug = True)
