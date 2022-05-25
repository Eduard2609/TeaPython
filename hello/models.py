from datetime import datetime
from hello import db

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    sugestion = db.relationship('Suggestion', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Application(db.Model):
    id_application = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    genre = db.Column(db.String(20), unique=True, nullable=False)
    install_command = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Application('{self.name}', '{self.description}', '{self.genre}', '{self.install_command}', '{self.image_file}')"

class Suggestion(db.Model):
    id_suggestion = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    genre = db.Column(db.String(20), unique=True, nullable=False)
    install_command = db.Column(db.String(120), nullable=True)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    date_sugested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)


    def __repr__(self):
        return f"Suggestion('{self.name}', '{self.description}', '{self.genre}', '{self.image_file}', '{self.date_sugested}')"
