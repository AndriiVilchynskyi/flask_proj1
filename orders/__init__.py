from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orders.db"
db = SQLAlchemy(app)

from orders import routes

