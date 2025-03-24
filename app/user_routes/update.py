from flask import Blueprint, request, jsonify
from app.database.database import db_session
from app.models.models import UserModel

update = Blueprint('update', __name__)

@update.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = UserModel.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    user_data = request.get_json()
    if not user_data:
        return jsonify({'error': 'No data provided'}), 400

    if 'email' in user_data:
        updated_email = user_data['email']
        existing_user = UserModel.query.filter_by(email=updated_email).first()
        if existing_user and existing_user.id != user_id:
            return jsonify({'error': 'Email already exists'}), 400
    
    
    for key, value in user_data.items():
        setattr(user, key, value)

    try:
        db_session.add(user)
        db_session.commit()
        return jsonify({
            'message': 'User updated successfully',
            'user': user.show_user()
        }), 200
    except Exception as e:
        db_session.rollback() 
        return jsonify({'error': f'Error updating user: {str(e)}'}), 500