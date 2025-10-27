# models/models.py
import mysql.connector
from config import DB_CONFIG

# --- Database connection helper ---
def get_connection():
    """Return a new MySQL connection using DB_CONFIG from config.py"""
    return mysql.connector.connect(**DB_CONFIG)


# --- Create all tables ---
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(150),
        role VARCHAR(50)
    )''')

    # Students table
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(120) NOT NULL,
        gender VARCHAR(10),
        class_name VARCHAR(50)
    )''')

    # Subjects table
    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        code VARCHAR(30)
    )''')

    # Scores table (added term column)
    cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT NOT NULL,
        subject_id INT NOT NULL,
        midterm FLOAT DEFAULT 0,
        final FLOAT DEFAULT 0,
        assignment FLOAT DEFAULT 0,
        total FLOAT,
        grade VARCHAR(3),
        term VARCHAR(20) DEFAULT 'Term1',
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
    )''')

    conn.commit()
    cursor.close()
    conn.close()


# --- User helper ---
class UserModel:
    @staticmethod
    def get_user_by_id(user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

# Optionally, you can import StudentModel, SubjectModel, ScoreModel here
# from .student_model import StudentModel
# from .subject_model import SubjectModel
# from .score_model import ScoreModel
