import mysql.connector
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config import get_connection  # your existing DB connection function

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

class UserModel:

    @staticmethod
    def get_user(username):
        """Fetch a user by username"""
        db = get_connection()
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            return cursor.fetchone()
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def get_user_by_id(user_id):
        """Fetch a user by id"""
        db = get_connection()
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def create_user(username, password, email=None, role='user'):
        """Create a new user with hashed password"""
        hashed_pw = generate_password_hash(password)
        db = get_connection()
        try:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)",
                (username, hashed_pw, email, role)
            )
            db.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def check_password(password, hashed):
        """Check password hash"""
        return check_password_hash(hashed, password)
