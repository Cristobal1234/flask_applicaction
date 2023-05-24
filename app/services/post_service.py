from app.models.post import Post
from app.repositories.post_repository import PostRepository



class PostService:
    def __init__(self):
        self.post_repository = PostRepository()

    def get_all_posts(self):
        return self.post_repository.get_all_posts()

    def get_post_by_id(self, post_id):
        return self.post_repository.get_post_by_id(post_id)

    def create_post(self, title, content, user_id):
        return self.post_repository.create_post(title, content, user_id)

    def update_post(self, post):
        return self.post_repository.update_post(post)

    def delete_post(self, post):
        return self.post_repository.delete_post(post)