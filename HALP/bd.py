import os

from cs50 import SQL
from flask import Flask
from flask_session import Session

from helpers import usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    hash = db.Column(db.String(60), nullable=False)
    stocks = db.relationship('stock', backref='owner', lazy=True)

    def __repr__(self):
        return f"users('{self.username}')"


class Stock(db.Model):
    StockIDid = db.Column(db.Integer, primary_key=True)
    Symbol = db.Column(db.String(100), nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.Symbol}')"
