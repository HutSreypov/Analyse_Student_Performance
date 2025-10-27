from flask import Blueprint, render_template, request, redirect, url_for
from models.score_model import ScoreModel
from models.student_model import StudentModel
from models.subject_model import SubjectModel
from flask_login import login_required

score_bp = Blueprint('score_bp', __name__, url_prefix='/scores')

# List all scores
@score_bp.route('/')
@login_required
def list_scores():  # ← this is the correct function name for url_for
    scores = ScoreModel.get_all()
    students = StudentModel.get_all()
    subjects = SubjectModel.get_all()
    return render_template('scores.html', scores=scores, students=students, subjects=subjects)

# Add a new score
@score_bp.route('/add', methods=['POST'])
@login_required
def add_score():
    student_id = request.form.get('student_id')
    subject_id = request.form.get('subject_id')
    midterm = float(request.form.get('midterm', 0))
    final = float(request.form.get('final', 0))
    assignment = float(request.form.get('assignment', 0))
    term = request.form.get('term', 'Term1')

    if student_id and subject_id:
        ScoreModel.add_score(student_id, subject_id, midterm, final, assignment, term)
    
    return redirect(url_for('score_bp.list_scores'))  # ← must match function name
