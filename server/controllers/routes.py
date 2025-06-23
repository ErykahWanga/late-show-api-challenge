from flask import Blueprint, jsonify
from server.models import db
from server.models.comedian import Comedian
from server.models.guest import Guest
from server.models.appearance import Appearance

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    return jsonify({"message": "Welcome to the Late Show API"})
