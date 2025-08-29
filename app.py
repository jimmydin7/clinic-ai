from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from utils import auth
from utils.images import images
from datetime import datetime, date
import pandas as pd
from models.cancer.cancer import predict as cancer_predict
from utils.cancer_utils import cancer_vars
from utils.cancer_utils.bmi_class import bmi_class
from utils.mental_health_vars import mental_health_questions, mental_health_scoring, MAX_SCORE, score_ranges

app = Flask(__name__)
app.secret_key = "dont-be-stupid-and-change-this-in-prod"

DB_PATH = 'instance\db.json'
dbHandler = auth.DBController(db_path=DB_PATH)


cancer_questions = cancer_vars.cancer_questions
cancer_option_maps = cancer_vars.cancer_option_maps

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
    return render_template('index.html', session=session, images=images)

@app.route('/login', methods=["GET", "POST"])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if dbHandler.validate_user(username, password):
            session['username'] = username

            user = dbHandler.get_user(username)
            if user and 'age' in user:
                session['age'] = user['age']
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
        birthday_str = request.form.get("birthday")

        age = None
        if birthday_str:
            try:
                birth_date = datetime.strptime(birthday_str, "%Y-%m-%d").date()
                today = date.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            except ValueError:
                flash("Invalid birthday format.", "danger")
                return redirect(url_for("register"))

        if dbHandler.add_user(username, password, birthday=birthday_str, age=age):
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
        session.pop('age', None)
        flash(f"Goodbye, {username}! You have been logged out.", "info")
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    username = session['username']
    test_results = dbHandler.get_user_test_results(username)
    
    cancer_results = [r for r in test_results if r['test_type'] == 'cancer']
    diabetes_results = [r for r in test_results if r['test_type'] == 'diabetes']
    mental_health_results = [r for r in test_results if r['test_type'] == 'mental_health']
    
    profile_data = {
        'cancer_results': cancer_results,
        'diabetes_results': diabetes_results,
        'mental_health_results': mental_health_results,
    }
    
    return render_template('dashboard.html', session=session, profile_data=profile_data)

@app.route('/cancer-test')
@login_required
def cancer_test():
    session['cancer_answers'] = {}
    return redirect(url_for('cancer_question', qid=0))

@app.route('/cancer-question/<int:qid>', methods=['GET', 'POST'])
@login_required
def cancer_question(qid):
    if qid >= len(cancer_questions):
        return redirect(url_for('cancer_summary'))
    
    question = cancer_questions[qid]
    
    if request.method == 'POST':
        answer = request.form.get('answer')
        
        if question['type'] == 'select':
            answer_text = question['options'][int(answer)]
            session['cancer_answers'][question['name']] = answer_text
        else:
            session['cancer_answers'][question['name']] = answer
        
        session.modified = True
        return redirect(url_for('cancer_question', qid=qid+1))
    
    return render_template('cancer-question.html', question=question, qid=qid)

@app.route('/cancer-summary')
@login_required
def cancer_summary():
    answers = session.get('cancer_answers', {})
    
    if not answers:
        flash("No cancer assessment data found. Please start the assessment.", "warning")
        return redirect(url_for('cancer_test'))
    

    model_input = {}
    for q in cancer_questions:
        name = q['name']
        val = answers.get(name)
        if q['type'] == 'select':
            val = cancer_option_maps[name][val]
        elif q['type'] == 'number':
            val = float(val) if '.' in str(val) else int(val)
        model_input[name] = val
    

    weight = float(model_input.pop('Weight'))
    height_cm = float(model_input.pop('Height'))
    height_m = height_cm / 100.0
    bmi = weight / (height_m ** 2)
    model_input['BMI'] = bmi
    
    bmi_classification, bmi_color = bmi_class(bmi)
    
    bmi_css_color = {
        'Green': '#059669',
        'Orange': '#d97706',
        'Red': '#dc2626'
    }.get(bmi_color, '#6b7280')
    

    feature_order = ['Age', 'Gender', 'BMI', 'Smoking', 'GeneticRisk', 'PhysicalActivity', 'AlcoholIntake', 'CancerHistory']
    ordered_input = {k: model_input[k] for k in feature_order}
    df = pd.DataFrame([ordered_input])

    probability = cancer_predict(df)
    

    if probability is not None:
        if probability >= 80:
            color = 'red-600'
            result = f"High risk: {probability:.2f}% chance of cancer."
        elif probability >= 50:
            color = 'orange-400'
            result = f"Medium risk: {probability:.2f}% chance of cancer."
        else:
            color = 'green-600'
            result = f"Low risk: {probability:.2f}% chance of cancer."
    else:
        color = 'green-600'
        result = "Low risk: Model predicts no cancer."
    

    age = model_input['Age']
    age_group_start = (age // 10) * 10
    age_group_end = age_group_start + 9
    

    avg_probability = 15.0
    
    test_data = {
        'bmi': round(bmi, 1),
        'bmi_class': bmi_classification,
        'smoking_times': answers.get('Smoking', 'Unknown'),
        'alcohol_times': answers.get('AlcoholIntake', 'Unknown'),
        'workout_times': answers.get('PhysicalActivity', 'Unknown'),
        'cancer_risk': probability if probability is not None else 0,
        'risk_level': 'High' if probability >= 80 else 'Medium' if probability >= 50 else 'Low',
        'age': age,
        'gender': answers.get('Gender', 'Unknown'),
        'weight': weight,
        'height': height_cm
    }
    
    username = session['username']
    dbHandler.save_test_result(username, 'cancer', test_data)
    
    return render_template('cancer-summary.html', 
                         answers=answers, 
                         result=result, 
                         color=color, 
                         user_probability=probability if probability is not None else 0,
                         avg_probability=avg_probability,
                         age_group=f"{age_group_start}-{age_group_end}",
                         bmi_classification=bmi_classification,
                         bmi_color=bmi_css_color,
                         bmi_value=f"{bmi:.1f}")

@app.route('/diabetes-test')
@login_required
def diabetes_test():
    return 'diabetes test here'

@app.route('/mental-health-test')
@login_required
def mental_health_test():
    session['mental_health_answers'] = {}
    return redirect(url_for('mental_health_question', qid=0))

@app.route('/mental-health-question/<int:qid>', methods=['GET', 'POST'])
@login_required
def mental_health_question(qid):
    if qid >= len(mental_health_questions):
        return redirect(url_for('mental_health_summary'))
    
    question = mental_health_questions[qid]
    
    if request.method == 'POST':
        answer = request.form.get('answer')
        
        if question['type'] == 'select':
            answer_text = question['options'][int(answer)]
            session['mental_health_answers'][question['name']] = answer_text
        
        session.modified = True
        return redirect(url_for('mental_health_question', qid=qid+1))
    
    return render_template('mental-health-question.html', question=question, qid=qid)

@app.route('/mental-health-summary')
@login_required
def mental_health_summary():
    answers = session.get('mental_health_answers', {})
    
    if not answers:
        flash("No mental health assessment data found. Please start the assessment.", "warning")
        return redirect(url_for('mental_health_test'))
    

    total_score = 0
    for question_name, answer in answers.items():
        if question_name in mental_health_scoring:
            total_score += mental_health_scoring[question_name][answer]
    

    percentage = (total_score / MAX_SCORE) * 100

    if percentage >= 80:
        color = 'green-600'
        result = f"Excellent mental health: {percentage:.1f}%"
        level = 'Excellent'
    elif percentage >= 60:
        color = 'blue-600'
        result = f"Good mental health: {percentage:.1f}%"
        level = 'Good'
    elif percentage >= 40:
        color = 'yellow-600'
        result = f"Fair mental health: {percentage:.1f}%"
        level = 'Fair'
    elif percentage >= 20:
        color = 'orange-600'
        result = f"Poor mental health: {percentage:.1f}%"
        level = 'Poor'
    else:
        color = 'red-600'
        result = f"Critical mental health: {percentage:.1f}%"
        level = 'Critical'
    

    test_data = {
        'total_score': total_score,
        'percentage': round(percentage, 1),
        'level': level,
        'max_score': MAX_SCORE,
        'answers': answers,
        'timestamp': datetime.now().isoformat()
    }
    
    username = session['username']
    dbHandler.save_test_result(username, 'mental_health', test_data)
    
    return render_template('mental-health-summary.html', 
                         answers=answers, 
                         result=result, 
                         color=color, 
                         percentage=percentage,
                         total_score=total_score,
                         max_score=MAX_SCORE,
                         level=level)

if __name__ == '__main__':
    app.run(debug=True)