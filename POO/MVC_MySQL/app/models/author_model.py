from app import db
class authors(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    book = db.relationship('books', backref='authors')
   
    def _repr__ (self):
        return '<Author {}>'.format(self.nome)