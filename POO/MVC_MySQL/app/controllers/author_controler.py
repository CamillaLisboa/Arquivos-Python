from app import app
from flask import Flask, render_template, request, redirect, url_for, Blueprint
from app.services import author_service

author_bp = Blueprint('author', __name__)

@author_bp.route('/', methods=['GET'])

def authors():
    print("pág home")
    autores = author_service.listar()
    return render_template('authors.html', autores=autores)

@author_bp.route('/add', methods=['POST'])
def add_author():
    nome = request.form.get('name')
    author_service.inserir(nome)
    return redirect(url_for('author.authors'))

@author_bp.route('/delete/<int:author_id>', methods=['GET'])
def delete_author(author_id):
    author_service.excluir(author_id)
    return redirect(url_for('author.authors'))

@author_bp.route('/autos/<int:author_id>', methods=['GET', 'POST'])
def atualiza_autor(author_id):
    autor = author_service.recupera_autor(author_id)
    if request.method == 'POST':
        nome = request.form.get('name')
        author_service.atualiza_autor(author_id, nome)
        return redirect(url_for('author.authors'))
    return render_template('edit_author.html', autor=autor)