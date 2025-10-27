from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from models.user_model import UserModel, User

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

# --- Login route ---
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user_data = UserModel.get_user(username)
        if user_data and UserModel.check_password(password, user_data['password']):
            # login_user requires an object that implements UserMixin
            login_user(User(id=user_data['id'], username=user_data['username']))
            return redirect(url_for("index"))

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


# --- Logout route ---
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))


# --- Register route ---
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm:
            return render_template("register.html", error="Passwords do not match")

        if UserModel.get_user(username):
            return render_template("register.html", error="Username already exists")

        UserModel.create_user(username, password)
        return redirect(url_for("auth_bp.login"))

    return render_template("register.html")
