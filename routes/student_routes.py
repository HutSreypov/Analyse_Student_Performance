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

@student_bp.route('/edit/<int:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    student = StudentModel.get_by_id(student_id)
    if not student:
        return redirect(url_for('student_bp.list_students'))
    if request.method == 'POST':
        StudentModel.update_student(student_id,
                                    request.form.get('name'),
                                    request.form.get('gender'),
                                    request.form.get('class_name'))
        return redirect(url_for('student_bp.list_students'))
    return render_template('edit_student.html', student=student)

@student_bp.route('/delete/<int:student_id>')
@login_required
def delete_student(student_id):
    StudentModel.delete_student(student_id)
    return redirect(url_for('student_bp.list_students'))

@student_bp.route('/progress/<int:student_id>')
@login_required
def student_progress(student_id):
    student = StudentModel.get_by_id(student_id)
    scores = StudentModel.get_progress(student_id)
    return render_template('progress.html', student=student, scores=scores)
