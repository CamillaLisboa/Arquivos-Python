from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

path = os.getcwd()
template_dir = os.path.abspath(os.path.join(path, os.pardir))
template_dir = os.path.join(template_dir, 'templates')
print(template_dir)
app = Flask(__name__, template_folder=template_dir)
app.config.from_object ('config')
db = SQLAlchemy(app)
from .models import book_model, author_model
from .services import book_service, author_service
from .controlers import book_controler, author_controler, home_controler
app.register_blueprint(book_controler.book_bp, url_prefix = '/book')
app.register_blueprint(author_controler.author_bp, url_prefix = '/author')
app.register_blueprint(home_controler.home_bp, url_prefix = '/')
with app.app_context():
    db.create_all()