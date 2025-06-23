from server.config import db

class Comedian(db.Model):
    __tablename__ = 'comedians'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String)

    appearances = db.relationship('Appearance', back_populates='comedian')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nationality': self.nationality
        }
