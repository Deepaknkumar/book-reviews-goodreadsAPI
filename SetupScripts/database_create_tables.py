"""Script to create new Tables in the database, BEWARE: It deletes the tables if they exist"""

import os
import database_scripts as dbs

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# def get_database_connection():
#     engine = create_engine(os.getenv("DATABASE_URL"))
#     db = scoped_session(sessionmaker(bind=engine))
#     return db

def populate_books():
    conn = dbs.get_database_connection()
    books_sql_1 = "DROP TABLE IF EXISTS books";
    books_sql_2 = """
    CREATE TABLE books(
    isbn VARCHAR NOT NULL PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year INTEGER
    );"""
    print("Droping/Creating books Table")
    conn.execute(books_sql_1)
    conn.commit()
    conn.execute(books_sql_2)
    conn.commit()
    print("books table created.")

def populate_users():
    conn = dbs.get_database_connection()
    users_sql_1 = "DROP TABLE IF EXISTS users"
    users_sql_2 = """
    CREATE TABLE users(
    userid SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    passwordsalt VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    datecreated DATE NOT NULL DEFAULT CURRENT_DATE 
    );"""
    print("Droping/Creating Users Table")
    conn.execute(users_sql_1)
    conn.commit()
    conn.execute(users_sql_2)
    conn.commit()
    print("Users table created.")

def populate_bookreviews():
    conn = dbs.get_database_connection()
    brs_sql_1 = "DROP TABLE IF EXISTS bookreviews"
    brs_sql_2 = """
        CREATE TABLE bookreviews(
        reviewid SERIAL PRIMARY KEY,
        userid INTEGER NOT NULL REFERENCES users,
        bookisbn VARCHAR NOT NULL REFERENCES books,
        review VARCHAR NOT NULL,
        dateposted TIMESTAMP DEFAULT now() 
        );"""
    print("Droping/Creating bookreviews Table")
    conn.execute(brs_sql_1)
    conn.commit()
    conn.execute(brs_sql_2)
    conn.commit()
    print("bookreviews table created.")

# populate_books()
# populate_users()
# populate_bookreviews()




