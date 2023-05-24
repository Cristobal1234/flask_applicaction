from app.repositories.comment_repository import CommentRepository



class CommentService:
    def __init__(self):
        self.comment_repo = CommentRepository()

    def get_all_comments(self):
        return self.comment_repo.get_all_comments()

    def get_comment(self, comment_id):
        return self.comment_repo.get_comment_by_id(comment_id)

    def create_comment(self, content, post_id, user_id):
        return self.comment_repo.create_comment(content, post_id, user_id)

    def update_comment(self, comment_id, content):
        return self.comment_repo.update_comment(comment_id, content)

    def delete_comment(self, comment_id):
        return self.comment_repo.delete_comment(comment_id)