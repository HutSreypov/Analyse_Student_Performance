from config import get_connection

class SubjectModel:
    @staticmethod
    def get_all():
        db = get_connection()
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM subjects")
            return cursor.fetchall()
        finally:
            cursor.close()
            db.close()
    
    @staticmethod
    def get_by_id(subject_id):
        db = get_connection()
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM subjects WHERE id = %s", (subject_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            db.close()
    
    @staticmethod
    def add_subject(name, code):
        db = get_connection()
        try:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO subjects (name, code) VALUES (%s, %s)",
                (name, code)
            )
            db.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            db.close()
    
    @staticmethod
    def delete_subject(subject_id):
        db = get_connection()
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM subjects WHERE id = %s", (subject_id,))
            db.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            db.close()
            
    @staticmethod
    def update_subject(subject_id, name, code):
        db = get_connection()
        try:
            cursor = db.cursor()
            cursor.execute(
                "UPDATE subjects SET name = %s, code = %s WHERE id = %s",
                (name, code, subject_id)
            )
            db.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            db.close()
