from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user

# --- Blueprints ---
from routes.student_routes import student_bp
from routes.subject_routes import subject_bp
from routes.score_routes import score_bp
from routes.analysis_routes import analysis_bp
from routes.api_routes import api_bp
from routes.auth_routes import auth_bp

# --- User model ---
from models.user_model import UserModel, User

# --- App Setup ---
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "your-secret-key"

# --- Flask-Login setup ---
login_manager = LoginManager(app)
login_manager.login_view = "auth_bp.login"

@login_manager.user_loader
def load_user(user_id):
    user_data = UserModel.get_user_by_id(user_id)
    if user_data:
        return User(id=user_data['id'], username=user_data.get('username') or user_data.get('name'))
    return None

# --- Register Blueprints ---
for bp in [student_bp, subject_bp, score_bp, analysis_bp, api_bp, auth_bp]:
    app.register_blueprint(bp)

# --- Home page ---
@app.route('/')
@login_required
def index():
    username = getattr(current_user, "username", None) or getattr(current_user, "name", "User")
    return render_template('index.html', username=username)

# --- Health check ---
@app.route('/status')
def status():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
