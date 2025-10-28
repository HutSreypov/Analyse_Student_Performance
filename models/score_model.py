from config import get_connection

class ScoreModel:

    @staticmethod
    def get_all_scores():
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT s.id, st.name AS student_name, sub.name AS subject_name,
                   s.midterm, s.assignment, s.final, s.total, s.grade
            FROM scores s
            JOIN students st ON s.student_id = st.id
            JOIN subjects sub ON s.subject_id = sub.id
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    @staticmethod
    def add_score(student_id, subject_id, midterm, assignment, final):
        total = float(midterm) + float(assignment) + float(final)
        grade = ScoreModel.calculate_grade(total)
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO scores (student_id, subject_id, midterm, assignment, final, total, grade) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (student_id, subject_id, midterm, assignment, final, total, grade)
        )
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def get_by_id(score_id):
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM scores WHERE id=%s", (score_id,))
        score = cursor.fetchone()
        cursor.close()
        db.close()
        return score

    @staticmethod
    def update_score(score_id, student_id, subject_id, midterm, assignment, final):
        total = float(midterm) + float(assignment) + float(final)
        grade = ScoreModel.calculate_grade(total)
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE scores SET student_id=%s, subject_id=%s, midterm=%s, assignment=%s, final=%s, total=%s, grade=%s WHERE id=%s",
            (student_id, subject_id, midterm, assignment, final, total, grade, score_id)
        )
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def delete_score(score_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM scores WHERE id=%s", (score_id,))
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def calculate_grade(total):
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
