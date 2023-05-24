from app.database import db
from app.models.comment import Comment



class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('posts', lazy=True))
    #comments = db.relationship('Comment', backref='post', lazy=True)
    comments = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)
    #tags = db.relationship('Tag', backref=db.backref('post', lazy=True))

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
        }