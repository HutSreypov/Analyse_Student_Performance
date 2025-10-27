from flask import Blueprint, jsonify
from models.score_model import ScoreModel
from models.student_model import StudentModel

# Make sure the blueprint variable name is exactly api_bp
api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

@api_bp.route('/student/<int:student_id>/progress')
def student_progress_api(student_id):
    student = StudentModel.get_by_id(student_id)
    if not student:
        return jsonify({"error": "student not found"}), 404

    scores = ScoreModel.get_by_student(student_id)
    return jsonify({
        "student": student,
        "scores": scores
    })
