"""Script to create new Tables in the database"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

def get_database_connection():
    engine = create_engine(os.getenv("DATABASE_URL"))
    db = scoped_session(sessionmaker(bind=engine))
    return db

def populate():
    conn = get_database_connection()
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

populate()



