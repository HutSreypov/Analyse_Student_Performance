# app.py
import sys
import os
from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user


# --- Ensure parent folder is in path to find models and routes ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- Blueprints ---
from routes.student_routes import student_bp
from routes.subject_routes import subject_bp
from routes.score_routes import score_bp
from routes.analysis_routes import analysis_bp
from routes.api_routes import api_bp
from routes.auth_routes import auth_bp

# --- User model helpers ---
from models.user_model import UserModel, User

# --- Flask app setup ---
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "your-secret-key"  # replace with a secure secret in production

# --- Flask-Login setup ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_bp.login"  # redirect unauthenticated users

@login_manager.user_loader
def load_user(user_id):
    """
    Called by Flask-Login to reload a user from the session.
    """
    user_data = UserModel.get_user_by_id(user_id)
    if not user_data:
        return None
    try:
        # Return a User object compatible with Flask-Login
        return User(id=user_data['id'], username=user_data.get('username') or user_data.get('name'))
    except Exception:
        return None

# --- Register blueprints ---
app.register_blueprint(student_bp)
app.register_blueprint(subject_bp)
app.register_blueprint(score_bp)
app.register_blueprint(analysis_bp)
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)

# --- Protected home page ---
@app.route('/')
@login_required
def index():
    """
    Home page, requires login.
    """
    username = getattr(current_user, "username", None) or getattr(current_user, "name", "User")
    return render_template('index.html', username=username)

# --- Optional health check ---
@app.route('/status')
def status():
    return {"status": "ok"}



# --- Run Flask app ---
if __name__ == '__main__':
    # Use debug=True only in development
    app.run(debug=True, port=5000)

