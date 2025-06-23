from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comedian(db.Model):
    __tablename__ = 'comedians'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)
    appearances = db.relationship('Appearance', backref='comedian', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nationality': self.nationality
        }

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comedian_id = db.Column(db.Integer, db.ForeignKey('comedians.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'comedian': self.comedian.to_dict(),
            'guest': self.guest.to_dict()
        }
