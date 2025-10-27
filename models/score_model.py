# models/score_model.py
from mysql.connector import ProgrammingError, Error
from config import get_connection

class ScoreModel:
    @staticmethod
    def get_all():
        """
        Returns list of score rows with student name and subject name.
        Assumes:
          - scores table has column `term`
          - students table has `id` and `name`
          - subjects table has `id` and `name`
        """
        db = get_connection()
        if not db:
            return []  # connection error handled in get_connection()

        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT
                    sc.id AS score_id,
                    sc.student_id,
                    st.name AS student_name,
                    sc.subject_id,
                    sub.name AS subject_name,
                    sc.midterm,
                    sc.final,
                    sc.assignment,
                    sc.total,
                    sc.grade,
                    sc.term
                FROM scores sc
                LEFT JOIN students st ON sc.student_id = st.id
                LEFT JOIN subjects sub ON sc.subject_id = sub.id
                ORDER BY sc.id;
            """)
            rows = cursor.fetchall()
            return rows
        except ProgrammingError as e:
            # SQL error (e.g., unknown column). Log & return empty list / or raise custom.
            print("SQL ProgrammingError in ScoreModel.get_all():", e)
            return []
        except Error as e:
            # Generic DB error
            print("MySQL Error in ScoreModel.get_all():", e)
            return []
        finally:
            try:
                cursor.close()
                db.close()
            except Exception:
                pass

    @staticmethod
    def get_by_id(score_id):
        db = get_connection()
        if not db:
            return None
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT sc.*, st.name AS student_name, sub.name AS subject_name
                FROM scores sc
                LEFT JOIN students st ON sc.student_id = st.id
                LEFT JOIN subjects sub ON sc.subject_id = sub.id
                WHERE sc.id = %s
            """, (score_id,))
            return cursor.fetchone()
        except Exception as e:
            print("Error in ScoreModel.get_by_id:", e)
            return None
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def create(score_data):
        """
        score_data: dict with keys: student_id, subject_id, midterm, final, assignment, total, grade, term
        """
        db = get_connection()
        if not db:
            return False
        cursor = db.cursor()
        try:
            cursor.execute("""
                INSERT INTO scores (student_id, subject_id, midterm, final, assignment, total, grade, term)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                score_data.get('student_id'),
                score_data.get('subject_id'),
                score_data.get('midterm'),
                score_data.get('final'),
                score_data.get('assignment'),
                score_data.get('total'),
                score_data.get('grade'),
                score_data.get('term'),
            ))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            print("Error in ScoreModel.create:", e)
            return False
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def update(score_id, score_data):
        db = get_connection()
        if not db:
            return False
        cursor = db.cursor()
        try:
            cursor.execute("""
                UPDATE scores
                SET student_id=%s, subject_id=%s, midterm=%s, final=%s, assignment=%s, total=%s, grade=%s, term=%s
                WHERE id=%s
            """, (
                score_data.get('student_id'),
                score_data.get('subject_id'),
                score_data.get('midterm'),
                score_data.get('final'),
                score_data.get('assignment'),
                score_data.get('total'),
                score_data.get('grade'),
                score_data.get('term'),
                score_id
            ))
            db.commit()
            return cursor.rowcount > 0
        except Exception as e:
            db.rollback()
            print("Error in ScoreModel.update:", e)
            return False
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def delete(score_id):
        db = get_connection()
        if not db:
            return False
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM scores WHERE id=%s", (score_id,))
            db.commit()
            return cursor.rowcount > 0
        except Exception as e:
            db.rollback()
            print("Error in ScoreModel.delete:", e)
            return False
        finally:
            cursor.close()
            db.close()
