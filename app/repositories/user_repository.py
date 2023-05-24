from app.models.user import User
from app.database import db

class UserRepository:
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def create_user(self, name, email, id):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self, user):
        db.session.commit()
        return user

    def delete_user(self, user):
        db.session.delete(user)
        db.session.commit()