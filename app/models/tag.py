from app.database import db



class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def __init__(self, name, post_id):
        self.name = name
        self.post_id = post_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'post_id': self.post_id,
        }