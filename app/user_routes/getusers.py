from flask import Blueprint, jsonify
from app.models.models import UserModel

getusers = Blueprint('getusers', __name__)

@getusers.route('/users', methods=['GET'])
def get_users():
    try:
        users = UserModel.query.all()
        if not users:
            return jsonify({'message': 'No users found'}), 404
        
        return jsonify({
            'message': 'Users retrieved successfully',
            'users': [user.show_user() for user in users]
        }), 200
    except Exception as e:
        return jsonify({'error': f'Error retrieving users: {str(e)}'}), 500