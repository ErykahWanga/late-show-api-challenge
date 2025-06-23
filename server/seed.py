from server.app import create_app
from server.models.models import db, Comedian, Guest, Appearance

app = create_app()

with app.app_context():
    print("Seeding data...")
    db.drop_all()
    db.create_all()

    c1 = Comedian(name='Trevor Noah', nationality='South African')
    c2 = Comedian(name='Ali Wong', nationality='American')

    g1 = Guest(name='Burna Boy', occupation='Musician')
    g2 = Guest(name='Chimamanda Adichie', occupation='Author')

    db.session.add_all([c1, c2, g1, g2])
    db.session.commit()

    a1 = Appearance(rating=5, comedian_id=c1.id, guest_id=g1.id)
    a2 = Appearance(rating=4, comedian_id=c2.id, guest_id=g2.id)

    db.session.add_all([a1, a2])
    db.session.commit()

    print("Seeding complete.")
