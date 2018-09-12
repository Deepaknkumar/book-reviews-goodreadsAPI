import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"
    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String,nullable=False)
    author = db.Column(db.String,nullable=False)
    year = db.Column(db.Integer)

class User(db.Model):
    __tablename__ = "users"
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    passwordsalt = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    datecreated = db.Column(db.DATE, nullable=False)

class BookReview(db.Model):
    __tablename__ = "bookreviews"
    reviewid = db.Column(db.Integer, primary_key=True)
