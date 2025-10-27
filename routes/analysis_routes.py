from flask import Blueprint, render_template
from flask_login import login_required
from models.score_model import ScoreModel

analysis_bp = Blueprint('analysis_bp', __name__, url_prefix='/analysis')

@analysis_bp.route('/')
@login_required
def analysis_index():
    """
    Analysis page:
    - Shows all scores
    - Computes class average per subject
    - Computes grade distribution
    """
    scores = ScoreModel.get_all()  # list of dicts with student_id, subject_id, total, grade
    
    # Compute class averages per subject
    subject_totals = {}
    subject_counts = {}
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    for s in scores:
        subject_id = s['subject_id']
        total = s['total'] or 0
        grade = s.get('grade', 'F')
        
        subject_totals[subject_id] = subject_totals.get(subject_id, 0) + total
        subject_counts[subject_id] = subject_counts.get(subject_id, 0) + 1
        
        if grade in grade_counts:
            grade_counts[grade] += 1
        else:
            grade_counts[grade] = 1
    
    subject_averages = {k: (subject_totals[k] / subject_counts[k]) for k in subject_totals}
    
    return render_template(
        'analysis.html',
        scores=scores,
        subject_averages=subject_averages,
        grade_counts=grade_counts
    )
