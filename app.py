from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from utils import auth

app = Flask(__name__)
app.secret_key = "dont-be-stupid-and-change-this-in-prod"

DB_PATH = 'instance\db.json'
dbHandler = auth.DBController(db_path=DB_PATH)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html', session=session)

@app.route('/login', methods=["GET", "POST"])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if dbHandler.validate_user(username, password):
            session['username'] = username
            flash(f"Welcome, {username}!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if dbHandler.add_user(username, password):
            flash("Account created successfully! Please log in.", "success")
            return redirect(url_for("login"))
        else:
            flash("Username already exists, try another.", "danger")
            return redirect(url_for("register"))

    return render_template("register.html")

@app.route('/logout')
def logout():
    if 'username' in session:
        username = session['username']
        session.pop('username', None)
        flash(f"Goodbye, {username}! You have been logged out.", "info")
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', session=session)

if __name__ == '__main__':
    app.run(debug=True)