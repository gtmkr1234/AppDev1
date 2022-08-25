import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./testdb.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)


class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    title = db.Column(db.String, unique=True)
    content = db.Column(db.String, unique=True)
    authors = db.relationship("User",secondary="article_authors")


class ArticleAuthors(db.Model):
    __tablename__ = 'article_authors'
    article_id = db.Column(db.Integer,db.ForeignKey("Article.article_id"), primary_key=True, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("User.user_id"), primary_key=True, nullable=False)


@app.route("/",methods =["GET","POST"] )
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        debug=True,
        port=5000
    )