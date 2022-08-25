import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "testdb.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.column(db.String, unique=True)
    email = db.column(db.String, unique=True)


class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.column(db.Integer,autoincrement=True, primary_key=True)
    title = db.column(db.String, unique=True)
    content = db.column(db.String, unique=True)
    authors = db.relationship("User",secondary="article_authors")


class ArticleAuthors(db.model):
    __tablename__ = 'article_authors'
    article_id = db.column(db.Integer,db.ForeignKey("Article.article_id"), primary_key=True, nullable=False)
    user_id = db.column(db.Integer,db.ForeignKey("User.user_id"), primary_key=True, nullable=False)


