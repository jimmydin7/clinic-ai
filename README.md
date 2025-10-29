clinic ai

overview

clinic ai is a simple flask web app for basic health self-assessments. it provides three flows:
- cancer risk questionnaire with bmi calculation and model-based probability
- diabetes risk questionnaire with model-based probability
- mental health questionnaire with scoring and level interpretation

users can register, log in, complete assessments, and view their saved results in a dashboard.

features

- authentication: registration, login, logout using a lightweight json store in `instance/db.json`
- assessments:
  - cancer: collects demographics and lifestyle, computes bmi and passes features to a model
  - diabetes: collects numeric clinical factors and predicts probability
  - mental health: collects qualitative answers, computes a percentage score and level
- dashboard: shows historical results by test type
- templating: html templates in `templates/` and static assets in `static/`

tech stack

- flask for the web framework
- jinja2 for templating
- pandas and numpy for data handling
- scikit-learn and joblib for model loading/inference

getting started

prerequisites

- python 3.10+
- pip

install dependencies

```bash
pip install -r requirements.txt
```

running the app (development)

```bash
python app.py
```

by default the app starts on `http://0.0.0.0:4646`.

configuration

- secret key: defined in `app.py` as `app.secret_key`. for production, set a secure secret via environment variable or config and do not commit secrets.
- database path: json file at `instance/db.json` (created on demand). ensure the `instance/` directory is writable.

main routes

- `/` home
- `/register` create an account
- `/login` log in
- `/logout` log out
- `/dashboard` view past results
- `/cancer-test` start cancer questionnaire
- `/cancer-question/<qid>` question-by-question flow
- `/cancer-summary` summary, bmi class, and model probability
- `/diabetes-test` start diabetes questionnaire
- `/diabetes-question/<qid>` question-by-question flow
- `/diabetes-summary` summary and model probability
- `/mental-health-test` start mental health questionnaire
- `/mental-health-question/<qid>` question-by-question flow
- `/mental-health-summary` summary, score, and level

model notes

- cancer: `models/cancer/cancer.py` exposes `predict(df)` and expects features including `age`, `gender`, `bmi`, `smoking`, `geneticrisk`, `physicalactivity`, `alcoholintake`, `cancerhistory`. bmi is computed from weight/height in the app.
- diabetes: `models/diabetes/diabetes.py` exposes `predict_diabetes(model_input)` and expects numeric fields such as `age`, `pregnancies`, `glucose`, `blood_pressure`, `skin_thickness`, `insulin`, `bmi`, `diabetes_pedigree`.
- mental health: scoring maps are defined in `utils/mental_health_vars.py`.

project structure

```text
.
├─ app.py                    # flask app entry point
├─ requirements.txt          # dependencies
├─ templates/                # jinja2 templates
├─ static/                   # css, js, images
├─ utils/                    # auth, variables, helpers
├─ models/                   # ml models and inference wrappers
├─ datasets/                 # sample or training datasets (if any)
├─ instance/                 # runtime json db (`db.json`)
├─ test_diabetes.py          # simple test for diabetes model
├─ license                   # license file
└─ readme.md                 # this file
```

development tips

- use a virtual environment to isolate dependencies
- set a secure `flask_secret_key` in production
- avoid storing real patient data; this is for educational and demonstration purposes only

testing

a basic test exists for diabetes logic:

```bash
python -m pytest -k diabetes -q
```

license

this project is provided under the terms of the license in `license`.

disclaimer

this software is not a medical device and does not provide medical advice. it is intended for educational and demonstration purposes only. always consult qualified healthcare professionals for medical decisions.
