from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def configure_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://prueba:prueba@db:5434/prueba'
    db.init_app(app)
    with app.app_context():
        db.create_all()