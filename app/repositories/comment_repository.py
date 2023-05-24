from app.models.tag import Tag
from app.models.comment import Comment
from app.database import db



class CommentRepository:
    def create_comment(self, content, post_id, user_id):
        comment = Comment(content=content, post_id=post_id, user_id=user_id)
        db.session.add(comment)
        db.session.commit()
        return comment

    def get_comment_by_id(self, comment_id):
        return Comment.query.get(comment_id)
    
    def get_all_comments(self):
        return Comment.query.all()

    def get_comments_by_post_id(self, post_id):
        return Comment.query.filter_by(post_id=post_id).all()

    def update_comment(self, comment_id, content):
        comment = self.get_comment_by_id(comment_id)
        if comment:
            comment.content = content
            db.session.commit()
        return comment

    def delete_comment(self, comment_id):
        comment = self.get_comment_by_id(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
        return comment