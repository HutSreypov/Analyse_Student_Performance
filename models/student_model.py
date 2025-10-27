from config import get_connection

class StudentModel:
    @staticmethod
    def get_all():
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
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
