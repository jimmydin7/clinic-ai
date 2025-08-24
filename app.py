from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/profile')
def profile():
    profile_data = {
        'name': 'jim',
        'password': 'das87b&!"*dsnw'
    }

    return render_template('profile.html', profile_data=profile_data)

app.run(debug=True)