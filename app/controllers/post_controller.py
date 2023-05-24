from flask import Blueprint, jsonify, request
from app.services.post_service import PostService



post_controller = Blueprint('post_controller', __name__)
post_service = PostService()


@post_controller.route('/posts', methods=['GET'])
def get_all_posts():
    posts = post_service.get_all_posts()
    serialized_posts = [post.to_dict() for post in posts]
    return jsonify(serialized_posts), 200

@post_controller.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = post_service.get_post_by_id(post_id)
    if post:
        return jsonify(post.to_dict()), 200
    return jsonify({'message': 'Post not found'}), 404

@post_controller.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = data.get('user_id')
    if title and content and user_id:
        post = post_service.create_post(title, content, user_id)
        return jsonify({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'user_id': post.user_id,
            'comments': post.comments,
        }), 200
    return jsonify({'message': 'Invalid request data'}), 400