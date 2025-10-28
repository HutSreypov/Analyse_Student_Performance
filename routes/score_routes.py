from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models.score_model import ScoreModel
from models.student_model import StudentModel
from models.subject_model import SubjectModel

score_bp = Blueprint('score_bp', __name__, url_prefix='/scores')

@score_bp.route('/')
@login_required
def list_scores():
    scores = ScoreModel.get_all_scores()
    students = StudentModel.get_all()
    subjects = SubjectModel.get_all()
    return render_template('scores.html', scores=scores, students=students, subjects=subjects)

@score_bp.route('/add', methods=['POST'])
@login_required
def add_score():
    ScoreModel.add_score(
        request.form.get('student_id'),
        request.form.get('subject_id'),
        request.form.get('midterm') or 0,
        request.form.get('assignment') or 0,
        request.form.get('final') or 0
    )
    return redirect(url_for('score_bp.list_scores'))

@score_bp.route('/edit/<int:score_id>', methods=['GET', 'POST'])
@login_required
def edit_score(score_id):
    score = ScoreModel.get_by_id(score_id)
    students = StudentModel.get_all()
    subjects = SubjectModel.get_all()
    if request.method == 'POST':
        ScoreModel.update_score(
            score_id,
            request.form.get('student_id'),
            request.form.get('subject_id'),
            request.form.get('midterm') or 0,
            request.form.get('assignment') or 0,
            request.form.get('final') or 0
        )
        return redirect(url_for('score_bp.list_scores'))
    return render_template('edit_score.html', score=score, students=students, subjects=subjects)

@score_bp.route('/delete/<int:score_id>')
@login_required
def delete_score(score_id):
    ScoreModel.delete_score(score_id)
    return redirect(url_for('score_bp.list_scores'))
