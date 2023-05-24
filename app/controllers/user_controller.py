from flask import Blueprint, jsonify, request
from app.services.user_service import UserService



user_controller = Blueprint('user_controller', __name__)
user_service = UserService()


@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404


@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name and email:
        user = user_service.create_user(name, email, id)
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 201
    return jsonify({'message': 'Invalid request data'}), 400