from flask import Blueprint, jsonify, request
from app.services.tag_service import TagService



tag_controller = Blueprint('tag', __name__)
tag_service = TagService()

@tag_controller.route('/tags', methods=['GET'])
def get_all_tags():
    tags = tag_service.get_all_tags()
    serialized_tags = [tag.to_dict() for tag in tags]
    return jsonify(serialized_tags), 200


@tag_controller.route('/tags/<int:tag_id>', methods=['GET'])
def get_tag(tag_id):
    tag = tag_service.get_tag(tag_id)
    if tag:
        return jsonify({
            'id': tag.id,
            'name': tag.name,
            'post_id': tag.post_id,
        }), 200
    return jsonify({'error': 'Tag not found'}), 404


@tag_controller.route('/tags', methods=['POST'])
def create_tag():
    name = request.json.get('name')
    post_id = request.json.get('post_id')
    tag = tag_service.create_tag(name, post_id)
    return jsonify({
            'id': tag.id,
            'name': tag.name,
            'post_id': tag.post_id,
        }), 200


@tag_controller.route('/tags/<int:tag_id>', methods=['PUT'])
def update_tag(tag_id):
    name = request.json.get('name')
    tag = tag_service.update_tag(tag_id, name)
    if tag:
        return jsonify({
            'id': tag.id,
            'name': tag.name,
            'post_id': tag.post_id,
        }), 200
    return jsonify({'error': 'Tag not found'}), 404


@tag_controller.route('/tags/<int:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    deleted = tag_service.delete_tag(tag_id)
    if deleted:
        return jsonify({'message': 'Tag deleted'}), 200
    return jsonify({'error': 'Tag not found'}), 404