from config import get_connection  # <- use the correct function name

class StudentModel:
    @staticmethod
    def get_all():
        db = get_connection()
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM students")
            return cursor.fetchall()
        finally:
            cursor.close()
            db.close()
    
    @staticmethod
    def get_by_id(student_id):
        db = get_connection()
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            db.close()
    
    @staticmethod
    def add_student(name, gender, class_name):
        db = get_connection()
        try:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO students (name, gender, class_name) VALUES (%s, %s, %s)",
                (name, gender, class_name)
            )
            db.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            db.close()

class StudentModel:
    @staticmethod
    def get_all():
        return [
            {"id": 1, "name": "Srey Pov", "gender": "F", "class_name": "10A"},
            {"id": 2, "name": "Chan Dara", "gender": "M", "class_name": "10B"},
            {"id": 3, "name": "Sothea", "gender": "F", "class_name": "10C"},
        ]

    @staticmethod
    def update_student(student_id, name=None, gender=None, class_name=None):
        db = get_connection()
        try:
            cursor = db.cursor()
            fields = []
            values = []
            if name:
                fields.append("name=%s")
                values.append(name)
            if gender:
                fields.append("gender=%s")
                values.append(gender)
            if class_name:
                fields.append("class_name=%s")
                values.append(class_name)
            if not fields:
                return False
            values.append(student_id)
            sql = f"UPDATE students SET {', '.join(fields)} WHERE id=%s"
            cursor.execute(sql, values)
            db.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def delete_student(student_id):
        db = get_connection()
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
            db.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            db.close()
