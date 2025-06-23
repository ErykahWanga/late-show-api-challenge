from flask import Blueprint, request, jsonify
from server.models.models import db, Comedian, Guest, Appearance

api = Blueprint('api', __name__)

@api.route('/comedians', methods=['GET'])
def get_comedians():
    comedians = Comedian.query.all()
    return jsonify([comedian.to_dict() for comedian in comedians]), 200

@api.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

@api.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([appearance.to_dict() for appearance in appearances]), 200

@api.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            comedian_id=data['comedian_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@api.route('/appearances/<int:id>', methods=['DELETE'])
def delete_appearance(id):
    appearance = Appearance.query.get(id)
    if appearance:
        db.session.delete(appearance)
        db.session.commit()
        return jsonify({'message': 'Appearance deleted'}), 200
    return jsonify({'error': 'Appearance not found'}), 404
