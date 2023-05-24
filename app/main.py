from flask import Flask
from app.controllers.user_controller import user_controller
from app.controllers.post_controller import post_controller
from app.controllers.tag_controller import tag_controller
from app.controllers.comment_controller import comment_controller
from app.database import configure_database

app = Flask(__name__)
app.register_blueprint(user_controller)
app.register_blueprint(post_controller)
app.register_blueprint(tag_controller)
app.register_blueprint(comment_controller)

configure_database(app)

if __name__ == '__main__':
    app.run()
    