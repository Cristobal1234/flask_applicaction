from flask import Blueprint, jsonify, request
from app.services.comment_service import CommentService



comment_controller = Blueprint('comment', __name__)
comment_service = CommentService()

@comment_controller.route('/comments', methods=['GET'])
def get_all_comments():
    comments = comment_service.get_all_comments()
    serialized_comments = [comment.to_dict() for comment in comments]
    return jsonify(serialized_comments), 200

@comment_controller.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = comment_service.get_comment(comment_id)
    if comment:
        return jsonify({
            'id': comment.id,
            'post_id': comment.post_id,
            'user_id': comment.user_id,
            'content': comment.content,
        }), 200
    return jsonify({'error': 'Comment not found'}), 404

@comment_controller.route('/comments', methods=['POST'])
def create_comment():
    content = request.json.get('content')
    post_id = request.json.get('post_id')
    user_id = request.json.get('user_id')
    comment = comment_service.create_comment(content, post_id, user_id)
    return jsonify({
            'id': comment.id,
            'post_id': comment.post_id,
            'user_id': comment.user_id,
            'content': comment.content,
        }), 200

@comment_controller.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    content = request.json.get('content')
    comment = comment_service.update_comment(comment_id, content)
    if comment:
        return jsonify({
            'id': comment.id,
            'post_id': comment.post_id,
            'user_id': comment.user_id,
            'content': comment.content,
        }), 200
    return jsonify({'error': 'Comment not found'}), 404

@comment_controller.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    deleted = comment_service.delete_comment(comment_id)
    if deleted:
        return jsonify({'message': 'Comment deleted'}), 200
    return jsonify({'error': 'Comment not found'}), 404