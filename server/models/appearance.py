from server.config import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    comedian_id = db.Column(db.Integer, db.ForeignKey('comedians.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))

    comedian = db.relationship('Comedian', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'comedian': self.comedian.to_dict(),
            'guest': self.guest.to_dict()
        }
