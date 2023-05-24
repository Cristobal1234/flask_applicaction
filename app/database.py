from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def configure_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:loquillo1995@127.0.0.1:5432/prueba'
    db.init_app(app)
    with app.app_context():
        db.create_all()