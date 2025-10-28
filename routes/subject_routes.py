from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
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

@subject_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_subject(id):
    subject = SubjectModel.get_by_id(id)
    if not subject:
        flash('Subject not found', 'error')
        return redirect(url_for('subject_bp.list_subjects'))
        
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        if name and code:
            SubjectModel.update_subject(id, name, code)
            flash('Subject updated successfully!', 'success')
            return redirect(url_for('subject_bp.list_subjects'))
        else:
            flash('Name and code are required', 'error')
    
    return render_template('edit_subject.html', subject=subject)

@subject_bp.route('/delete/<int:id>')
@login_required
def delete_subject(id):
    if SubjectModel.delete_subject(id):
        flash('Subject deleted successfully!', 'success')
    else:
        flash('Failed to delete subject', 'error')
    return redirect(url_for('subject_bp.list_subjects'))
