import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./testdb.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)


class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True)
    content = db.Column(db.String, unique=True)
    authors = db.relationship("User", secondary="article_authors")


class ArticleAuthors(db.Model):
    __tablename__ = 'article_authors'
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), primary_key=True, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey("article.article_id"), primary_key=True, nullable=False)


@app.route("/", methods=["GET", "POST"])
def articles():
    articles = Article.query.all()
    return render_template("articles.html", articles=articles)


@app.route("/articles_by/<user_name>", methods=["GET", "POST"])
def getArticles(user_name):
    articles = Article.query.filter(Article.authors.any(username=user_name))
    return render_template("article_by_authors.html", articles=articles)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
        port=5000
    )
