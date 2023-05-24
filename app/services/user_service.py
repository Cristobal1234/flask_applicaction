from app.models.user import User
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, name, email, id):
        return self.user_repository.create_user(name, email, id)

    def update_user(self, user):
        return self.user_repository.update_user(user)

    def delete_user(self, user):
        return self.user_repository.delete_user(user)