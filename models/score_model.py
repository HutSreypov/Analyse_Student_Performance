from config import get_connection

class ScoreModel:
    @staticmethod
    def get_grade(total):
        if total >= 90:
            return 'A'
        elif total >= 80:
            return 'B'
        elif total >= 70:
            return 'C'
        elif total >= 60:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def add_score(student_id, subject_id, midterm, final, assignment):
        total = midterm*0.3 + assignment*0.2 + final*0.5
        grade = ScoreModel.get_grade(total)

        db = get_connection()
        try:
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO scores (student_id, subject_id, midterm, final, assignment, total, grade)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (student_id, subject_id, midterm, final, assignment, total, grade))
            db.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def get_all():
        db = get_connection()
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.id, st.name AS student_name, sb.name AS subject_name,
                       s.midterm, s.final, s.assignment, s.total, s.grade
                FROM scores s
                JOIN students st ON s.student_id = st.id
                JOIN subjects sb ON s.subject_id = sb.id
            """)
            return cursor.fetchall()
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def get_by_student(student_id):
        db = get_connection()
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.id, sb.name AS subject_name, s.midterm, s.final, s.assignment, s.total, s.grade
                FROM scores s
                JOIN subjects sb ON s.subject_id = sb.id
                WHERE s.student_id=%s
            """, (student_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
            db.close()
