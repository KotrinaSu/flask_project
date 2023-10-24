from app import db

class Vyras(db.Model):
    __tablename__ = 'vyrai'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(80), nullable=False)
    amzius = db.Column(db.String(120), unique=True, nullable=False)
    ugis = db.Column(db.Text, nullable=False)
    svoris = db.Column(db.Text, nullable=False)

    def __init__(self, vardas, amzius, ugis, svoris):
        self.vardas = vardas
        self.amzius = amzius
        self.ugis = ugis
        self.svoris = svoris

    def __repr__(self):
        return f'{self.vardas} - {self.svoris}'