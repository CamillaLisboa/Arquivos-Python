from app.models.book_model import books
from app import db
 
def listar():
    livros = books.query.all()
    return livros
 
def inserir(nome):
    new_book = books(name = nome)
    db.session.add(new_book)
    db.session.commit()
 
def excluir(booknew_book_id):
    new_book = books.query.get(new_book_id)
    if new_book:
        db.session.delete(new_book)
        db.session.commit()
 
def recupera_book(book_id):
    book = books.query.filter_by(id = book_id).first()
    return book
 
def atualiza_book(id, name):
    books.query.filter_by(id = id).update({"name" : name})
    db.session.commit()