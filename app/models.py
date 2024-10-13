from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Table name in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(150), unique=True, nullable=False)  # Unique username
    password = db.Column(db.String(255), nullable=False)  # Password with increased length

    def __repr__(self):
        return f'<User {self.username}>'  # Representation of the User object

    def setPassword(self, password):
        self.password = generate_password_hash(password)  # Hash the password

    def checkPassword(self, password):
        return check_password_hash(self.password, password)  # Check hashed password

# User loader for Flask-Login
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Load user by ID
