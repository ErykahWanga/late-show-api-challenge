from flask import request

from flask import jsonify

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Late Show API!"})

@app.route("/appearances")
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([{
        "id": a.id,
        "rating": a.rating,
        "comedian": a.comedian.name,
        "guest": a.guest.name
    } for a in appearances])

@app.route("/comedians", methods=["POST"])
def create_comedian():
    data = request.get_json()
    new_comedian = Comedian(name=data["name"], nationality=data["nationality"])
    db.session.add(new_comedian)
    db.session.commit()
    return jsonify({"id": new_comedian.id}), 201

@app.route("/guests", methods=["POST"])
def create_guest():
    data = request.get_json()
    new_guest = Guest(name=data["name"], occupation=data["occupation"])
    db.session.add(new_guest)
    db.session.commit()
    return jsonify({"id": new_guest.id}), 201

@app.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()
    new_appearance = Appearance(
        rating=data["rating"],
        comedian_id=data["comedian_id"],
        guest_id=data["guest_id"]
    )
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify({"id": new_appearance.id}), 201
@app.route("/comedians/<int:id>", methods=["PUT"])
def update_comedian(id):
    comedian = Comedian.query.get_or_404(id)
    data = request.get_json()
    comedian.name = data.get("name", comedian.name)
    comedian.nationality = data.get("nationality", comedian.nationality)
    db.session.commit()
    return jsonify({"message": "Comedian updated"})

@app.route("/comedians/<int:id>", methods=["DELETE"])
def delete_comedian(id):
    comedian = Comedian.query.get_or_404(id)
    db.session.delete(comedian)
    db.session.commit()
    return jsonify({"message": "Comedian deleted"})

