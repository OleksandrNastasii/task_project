from flask import Blueprint, jsonify
from app.models.models import UserModel

getuser = Blueprint('getuser', __name__)

@getuser.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = UserModel.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'message': 'User retrieved successfully',
            'user': user.show_user()
        }), 200
    except Exception as e:
        return jsonify({'error': f'Error retrieving user: {str(e)}'}), 500