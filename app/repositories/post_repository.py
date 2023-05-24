from app.models.post import Post
from app.database import db

class PostRepository:
    def get_post_by_id(self, post_id):
        return Post.query.get(post_id)

    def create_post(self, title, content, user_id):
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return post
    
    def get_all_posts(self):
        return Post.query.all()

    def update_post(self, post):
        db.session.commit()
        return post

    def delete_post(self, post):
        db.session.delete(post)
        db.session.commit()