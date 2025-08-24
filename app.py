from flask import Flask, render_template, request, redirect, url_for, flash
from utils import auth

app = Flask(__name__)
app.secret_key = "dont-be-stupid-and-change-this-in-prod"

DB_PATH = 'instance\db.json'
dbHandler = auth.DBController(db_path=DB_PATH)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
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


app.run(debug=True)