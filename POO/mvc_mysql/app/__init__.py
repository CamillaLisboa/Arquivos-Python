from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

path = os.getcwd()
tempalte_dir = os.path.abspath(os.path.join(path, os.pardir))
template_dir = os.path.join(tempalte_dir, 'templates')
print(template_dir)

app = Flask(__name__, template_folder=template_dir)
app.config.from_object('config')
db = SQLAlchemy(app)

from.models import book_model, author_model
from .services import book_service, author_service
from.controllers import book_controller, author_controller, home_controller

app.register_blueprint(home_controller.home_bp, url_prefix='/')
app.register_blueprint(book_controller.book_bp, url_prefix='/book')  
app.register_blueprint(author_controller.author_bp, url_prefix='/author')

with app.app_context():
    db.create_all()
