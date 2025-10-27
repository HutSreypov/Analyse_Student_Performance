# migration/migrate_and_seed.py
import sys
import os

# Ensure parent folder is in path to find models/models.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from models/models.py
from models.models import create_tables, get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # --- Users table for Flask-Login ---
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            'INSERT INTO users (username, password, email, role) VALUES (%s,%s,%s,%s)',
            ('admin', 'admin123', 'admin@example.com', 'admin')
        )

    # --- Students ---
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            'INSERT INTO students (name, gender, class_name) VALUES (%s, %s, %s)',
            [
                ('Srey Pov Hut', 'F', '10A'),
                ('Chan Dara', 'M', '10A'),
                ('Som Khemara', 'M', '10B')
            ]
        )

    # --- Subjects ---
    cursor.execute("SELECT COUNT(*) FROM subjects")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            'INSERT INTO subjects (name, code) VALUES (%s, %s)',
            [
                ('Mathematics', 'MATH101'),
                ('English', 'ENG101'),
                ('Physics', 'PHY101')
            ]
        )

    # --- Scores ---
    cursor.execute("SELECT COUNT(*) FROM scores")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            '''INSERT INTO scores
               (student_id, subject_id, midterm, final, assignment, total, grade)
               VALUES (%s, %s, %s, %s, %s, %s, %s)''',
            [
                (1, 1, 85, 90, 80, (85*0.3 + 80*0.2 + 90*0.5), 'B'),
                (1, 2, 70, 75, 72, (70*0.3 + 72*0.2 + 75*0.5), 'C'),
                (1, 3, 95, 94, 96, (95*0.3 + 96*0.2 + 94*0.5), 'A'),
                (2, 1, 60, 55, 65, (60*0.3 + 65*0.2 + 55*0.5), 'D'),
                (3, 1, 78, 80, 75, (78*0.3 + 75*0.2 + 80*0.5), 'B')
            ]
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Database seeded successfully!")


if __name__ == "__main__":
    print("🚀 Running migration...")

    # Create tables first
    create_tables()
    print("📦 Tables created successfully!")

    # Seed initial data
    print("📦 Seeding data...")
    seed_data()
    print("🎉 Migration & seeding complete!")
