from flask import Blueprint, render_template, request, redirect, url_for

student_bp = Blueprint('student_bp', __name__, template_folder='../templates')

# In-memory storage for demonstration
students_data = [
    {"id": 1, "name": "Srey Pov", "gender": "F", "class_name": "10A"},
    {"id": 2, "name": "Chan Dara", "gender": "M", "class_name": "10B"},
]

@student_bp.route('/students', methods=['GET', 'POST'])
def list_students():
    if request.method == 'POST':
        new_id = max([s["id"] for s in students_data], default=0) + 1
        students_data.append({
            "id": new_id,
            "name": request.form['name'],
            "gender": request.form['gender'],
            "class_name": request.form['class_name']
        })
        return redirect(url_for('student_bp.list_students'))
    return render_template('students.html', students=students_data)

@student_bp.route('/students/<int:student_id>/progress')
def student_progress(student_id):
    student = next((s for s in students_data if s["id"] == student_id), None)
    if not student:
        return "Student not found", 404
    return render_template('student_progress.html', student=student)
