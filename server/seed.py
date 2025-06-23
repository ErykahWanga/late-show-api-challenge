from server.app import create_app
from server.models import db
from server.models.comedian import Comedian
from server.models.guest import Guest
from server.models.appearance import Appearance
from datetime import date

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    c1 = Comedian(name="Trevor Noah")
    c2 = Comedian(name="Ali Wong")
    g1 = Guest(name="Barack Obama")
    g2 = Guest(name="Zendaya")

    db.session.add_all([c1, c2, g1, g2])
    db.session.commit()

    a1 = Appearance(date=date(2023, 4, 1), guest=g1, comedian=c1)
    a2 = Appearance(date=date(2023, 5, 2), guest=g2, comedian=c2)

    db.session.add_all([a1, a2])
    db.session.commit()

    print("Database seeded!")
