from flask import Blueprint, jsonify
from flask_login import login_required
from models.score_model import ScoreModel
from models.student_model import StudentModel
from models.subject_model import SubjectModel

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

@api_bp.route('/student/<int:student_id>/progress')
@login_required  # optional: remove if you want public access
def student_progress_api(student_id):
    """
    Returns JSON with a student's progress:
    - student info
    - list of scores per subject with midterm, final, assignment, total, grade
    """
    student = StudentModel.get_by_id(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    scores = ScoreModel.get_by_student(student_id)
    
    # Optional: include subject names
    structured_scores = []
    for s in scores:
        subject = SubjectModel.get_by_id(s['subject_id'])
        structured_scores.append({
            "subject_id": s['subject_id'],
            "subject_name": subject['name'] if subject else "Unknown",
            "midterm": s.get('midterm', 0),
            "final": s.get('final', 0),
            "assignment": s.get('assignment', 0),
            "total": s.get('total', 0),
            "grade": s.get('grade', "F")
        })

    return jsonify({
        "student": student,
        "scores": structured_scores
    })
