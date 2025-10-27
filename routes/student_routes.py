from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models.student_model import StudentModel

student_bp = Blueprint('student_bp', __name__, url_prefix='/students')

@student_bp.route('/')
@login_required
def list_students():
    students = StudentModel.get_all()
    return render_template('students.html', students=students)

@student_bp.route('/add', methods=['POST'])
@login_required
def add_student():
    name = request.form.get('name')
    gender = request.form.get('gender')
    class_name = request.form.get('class_name')
    if name:
        StudentModel.add_student(name, gender, class_name)
    return redirect(url_for('student_bp.list_students'))

@student_bp.route('/progress/<int:student_id>')
@login_required
def student_progress(student_id):
    # Assuming you have a method in StudentModel to get progress (scores) for a student
    student = StudentModel.get_by_id(student_id)
    scores = StudentModel.get_progress(student_id)  # returns list of scores
    return render_template('progress.html', student=student, scores=scores)
