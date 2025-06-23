from server.models import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    comedian_id = db.Column(db.Integer, db.ForeignKey('comedians.id'))

    guest = db.relationship("Guest", back_populates="appearances")
    comedian = db.relationship("Comedian", back_populates="appearances")
