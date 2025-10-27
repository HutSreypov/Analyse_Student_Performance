from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models.subject_model import SubjectModel

subject_bp = Blueprint('subject_bp', __name__, url_prefix='/subjects')

@subject_bp.route('/')
@login_required
def list_subjects():
    subjects = SubjectModel.get_all()
    return render_template('subjects.html', subjects=subjects)

@subject_bp.route('/add', methods=['POST'])
@login_required
def add_subject():
    name = request.form.get('name')
    code = request.form.get('code')
    SubjectModel.add_subject(name, code)
    return redirect(url_for('subject_bp.list_subjects'))

@subject_bp.route('/delete/<int:id>')
@login_required
def delete_subject(id):
    SubjectModel.delete_subject(id)
    return redirect(url_for('subject_bp.list_subjects'))
