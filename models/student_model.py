from config import get_connection
from flask import request

class StudentModel:

    @staticmethod
    def get_all():
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students ORDER BY name ASC")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    @staticmethod
    def add_student(name, gender, class_name):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO students (name, gender, class_name) VALUES (%s, %s, %s)",
            (name, gender, class_name)
        )
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def get_by_id(student_id):
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
        student = cursor.fetchone()
        cursor.close()
        db.close()
        return student

    @staticmethod
    def update_student(student_id, name, gender, class_name):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE students SET name=%s, gender=%s, class_name=%s WHERE id=%s",
            (name, gender, class_name, student_id)
        )
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def delete_student(student_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def get_progress(student_id):
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT sb.name AS subject, s.midterm, s.final, s.assignment, s.total, s.grade
            FROM scores s
            JOIN subjects sb ON s.subject_id = sb.id
            WHERE s.student_id=%s
        """, (student_id,))
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data


def get_students():
    search = request.args.get('search', '')  # get query from URL
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE name LIKE %s ", (f"%{search}%",))
    students = cursor.fetchall()
    cursor.close()
    db.close()
