from server.models import db

class Comedian(db.Model):
    __tablename__ = 'comedians'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    appearances = db.relationship("Appearance", back_populates="comedian")
