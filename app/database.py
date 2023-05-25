from flask_sqlalchemy import SQLAlchemy
import os



db = SQLAlchemy()
db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '5432')
db_name = os.environ.get('DB_NAME', 'mydatabase')
db_user = os.environ.get('DB_USER', 'myuser')
db_password = os.environ.get('DB_PASSWORD', 'mypassword')

def configure_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}'
    db.init_app(app)
    with app.app_context():
        db.create_all()