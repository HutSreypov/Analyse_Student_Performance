# routes/analysis_routes.py
from flask import Blueprint, render_template
from models.models import get_connection

analysis_bp = Blueprint('analysis_bp', __name__)

@analysis_bp.route('/analysis')
def analysis_index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Join scores with subjects and students
    cursor.execute("""
        SELECT sc.id AS score_id, sc.student_id, sc.subject_id, sc.midterm, sc.final, sc.assignment, sc.total, sc.grade,
               sb.name AS subject_name, st.name AS student_name
        FROM scores sc
        JOIN subjects sb ON sc.subject_id = sb.id
        JOIN students st ON sc.student_id = st.id
        ORDER BY sc.student_id, sc.subject_id
    """)
    scores = cursor.fetchall()

    # Optional: organize by student or subject
    analysis_data = []
    for s in scores:
        analysis_data.append({
            'score_id': s['score_id'],
            'student_id': s['student_id'],
            'student_name': s['student_name'],
            'subject_id': s['subject_id'],
            'subject_name': s['subject_name'],
            'midterm': s['midterm'],
            'final': s['final'],
            'assignment': s['assignment'],
            'total': s['total'],
            'grade': s['grade']
        })

    cursor.close()
    conn.close()

    return render_template('analysis.html', scores=analysis_data)
