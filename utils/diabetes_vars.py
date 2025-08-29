diabetes_questions = [
    {
        'name': 'age',
        'label': 'What is your age?',
        'type': 'number',
        'min': 18,
        'max': 100
    },
    {
        'name': 'pregnancies',
        'label': 'How many times have you been pregnant? (0 if male or never pregnant)',
        'type': 'number',
        'min': 0,
        'max': 20
    },
    {
        'name': 'glucose',
        'label': 'What is your fasting glucose level (mg/dL)?',
        'type': 'number',
        'min': 50,
        'max': 300
    },
    {
        'name': 'blood_pressure',
        'label': 'What is your blood pressure (systolic, top number)?',
        'type': 'number',
        'min': 60,
        'max': 200
    },
    {
        'name': 'skin_thickness',
        'label': 'What is your skin thickness (mm)? (Use 20 if unsure)',
        'type': 'number',
        'min': 0,
        'max': 100
    },
    {
        'name': 'insulin',
        'label': 'What is your insulin level (mu U/ml)? (Use 0 if unsure)',
        'type': 'number',
        'min': 0,
        'max': 1000
    },
    {
        'name': 'bmi',
        'label': 'What is your BMI?',
        'type': 'number',
        'min': 15,
        'max': 60
    },
    {
        'name': 'diabetes_pedigree',
        'label': 'What is your diabetes pedigree function? (Use 0.5 if unsure)',
        'type': 'number',
        'min': 0,
        'max': 3,
        'step': 0.1
    }
]

diabetes_ranges = {
    'glucose': {'normal': (70, 99), 'prediabetes': (100, 125), 'diabetes': (126, 300)},
    'blood_pressure': {'normal': (90, 119), 'elevated': (120, 129), 'high': (130, 200)},
    'bmi': {'underweight': (15, 18.4), 'normal': (18.5, 24.9), 'overweight': (25, 29.9), 'obese': (30, 60)}
}
