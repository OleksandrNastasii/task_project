from flask import Blueprint, jsonify
from app.database.database import db_session
from app.models.models import UserModel

delete = Blueprint('delete', __name__)

@delete.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserModel.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    try:
        db_session.delete(user)
        db_session.commit()
        return jsonify({'message': f'User with ID {user_id} deleted successfully'}), 200
    except Exception as e:
        db_session.rollback() 
        return jsonify({'error': f'Error deleting user: {str(e)}'}), 500