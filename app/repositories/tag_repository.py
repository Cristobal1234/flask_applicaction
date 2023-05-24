from app.models.tag import Tag
from app.models.comment import Comment
from app.database import db



class TagRepository:
    def create_tag(self, name, post_id):
        tag = Tag(name=name, post_id=post_id)
        db.session.add(tag)
        db.session.commit()
        return tag

    def get_tag_by_id(self, tag_id):
        return Tag.query.get(tag_id)

    def get_all_tags(self):
        return Tag.query.all()

    def update_tag(self, tag_id, name):
        tag = self.get_tag_by_id(tag_id)
        if tag:
            tag.name = name
            db.session.commit()
        return tag

    def delete_tag(self, tag_id):
        tag = self.get_tag_by_id(tag_id)
        if tag:
            db.session.delete(tag)
            db.session.commit()
        return tag