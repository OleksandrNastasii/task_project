from flask import Blueprint, request, jsonify
from app.database.database import db_session
from app.models.models import UserModel
import re

create = Blueprint('create', __name__)

@create.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    if not user_data:
        return jsonify({'error': 'No data provided'}), 400

    required_fields = ['email', 'name']
    for field in required_fields:
        if field not in user_data:
            return jsonify({'error': f'{field} is required'}), 400

    email = user_data['email']
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'error': 'Invalid email format'}), 400

    existing_user = UserModel.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({
            'error': 'Email already exists',
            'existing_user_id': existing_user.id
        }), 400

    try:
        new_user = UserModel(**user_data)
        db_session.add(new_user)
        db_session.commit()
        return jsonify({
            'message': 'User created successfully',
            'id': new_user.id,
            'email': new_user.email,
            'name': new_user.name,
            'created_at': new_user.created_at
            }), 201
    except Exception as e:
        db_session.rollback()