cancer_questions = [
    {'name': 'Age', 'type': 'number', 'label': 'What is your age?'},
    {'name': 'Gender', 'type': 'select', 'label': 'What is your biological sex?', 'options': ['Female', 'Male']},
    {'name': 'Weight', 'type': 'number', 'label': 'What is your weight in kilograms (kg)?'},
    {'name': 'Height', 'type': 'number', 'label': 'What is your height in centimeters (cm)?'},
    {'name': 'Smoking', 'type': 'select', 'label': 'Do you currently smoke or have a history of smoking?', 'options': ['No', 'Yes']},
    {'name': 'GeneticRisk', 'type': 'select', 'label': 'Has any of your alive or dead relatives had cancer?', 'options': ['No', 'Some relatives', 'Many relatives']},
    {'name': 'PhysicalActivity', 'type': 'number', 'label': 'How many hours do you exercise per week? (e.g. 3)'},
    {'name': 'AlcoholIntake', 'type': 'number', 'label': 'How many alcoholic drinks do you have per week? (e.g. 2)'},
    {'name': 'CancerHistory', 'type': 'select', 'label': 'Have you ever been diagnosed with cancer before?', 'options': ['No', 'Yes']}
]

cancer_option_maps = {
    'Gender': {'Female': 0, 'Male': 1},
    'Smoking': {'No': 0, 'Yes': 1},
    'GeneticRisk': {'No': 0, 'Some relatives': 1, 'Many relatives': 2},
    'CancerHistory': {'No': 0, 'Yes': 1}
}