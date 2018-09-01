import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Check for GoodReads API key
if not os.getenv("GOODREADS_API_KEY"):
    raise RuntimeError("Goodreads API key is not set.")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Good Reads API Key
api_key = os.getenv("GOODREADS_API_KEY")

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights")
    return "Project 1: TODO"
