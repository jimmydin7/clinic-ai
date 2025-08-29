
mental_health_questions = [
    {
        'name': 'sleep_quality',
        'label': 'How would you rate your sleep quality over the past month?',
        'type': 'select',
        'options': ['Very Poor (1-2 hours)', 'Poor (3-4 hours)', 'Fair (5-6 hours)', 'Good (7-8 hours)', 'Excellent (8+ hours)']
    },
    {
        'name': 'stress_level',
        'label': 'How often do you feel stressed or overwhelmed?',
        'type': 'select',
        'options': ['Never', 'Rarely', 'Sometimes', 'Often', 'Almost Always']
    },
    {
        'name': 'mood_stability',
        'label': 'How stable has your mood been recently?',
        'type': 'select',
        'options': ['Very Unstable', 'Unstable', 'Somewhat Stable', 'Stable', 'Very Stable']
    },
    {
        'name': 'social_connections',
        'label': 'How satisfied are you with your social connections and relationships?',
        'type': 'select',
        'options': ['Very Dissatisfied', 'Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
    },
    {
        'name': 'energy_levels',
        'label': 'How would you describe your energy levels throughout the day?',
        'type': 'select',
        'options': ['Very Low', 'Low', 'Moderate', 'High', 'Very High']
    },
    {
        'name': 'concentration',
        'label': 'How well can you concentrate on tasks?',
        'type': 'select',
        'options': ['Very Poor', 'Poor', 'Fair', 'Good', 'Excellent']
    },
    {
        'name': 'appetite',
        'label': 'How has your appetite been recently?',
        'type': 'select',
        'options': ['Significantly Decreased', 'Decreased', 'Normal', 'Increased', 'Significantly Increased']
    },
    {
        'name': 'motivation',
        'label': 'How motivated do you feel to accomplish daily tasks?',
        'type': 'select',
        'options': ['Very Low', 'Low', 'Moderate', 'High', 'Very High']
    },
    {
        'name': 'anxiety_frequency',
        'label': 'How often do you experience anxiety or worry?',
        'type': 'select',
        'options': ['Never', 'Rarely', 'Sometimes', 'Often', 'Almost Always']
    },
    {
        'name': 'self_worth',
        'label': 'How do you generally feel about yourself and your self-worth?',
        'type': 'select',
        'options': ['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive']
    }
]


mental_health_scoring = {
    'sleep_quality': {'Very Poor (1-2 hours)': 1, 'Poor (3-4 hours)': 2, 'Fair (5-6 hours)': 3, 'Good (7-8 hours)': 4, 'Excellent (8+ hours)': 5},
    'stress_level': {'Never': 5, 'Rarely': 4, 'Sometimes': 3, 'Often': 2, 'Almost Always': 1},
    'mood_stability': {'Very Unstable': 1, 'Unstable': 2, 'Somewhat Stable': 3, 'Stable': 4, 'Very Stable': 5},
    'social_connections': {'Very Dissatisfied': 1, 'Dissatisfied': 2, 'Neutral': 3, 'Satisfied': 4, 'Very Satisfied': 5},
    'energy_levels': {'Very Low': 1, 'Low': 2, 'Moderate': 3, 'High': 4, 'Very High': 5},
    'concentration': {'Very Poor': 1, 'Poor': 2, 'Fair': 3, 'Good': 4, 'Excellent': 5},
    'appetite': {'Significantly Decreased': 1, 'Decreased': 2, 'Normal': 3, 'Increased': 4, 'Significantly Increased': 5},
    'motivation': {'Very Low': 1, 'Low': 2, 'Moderate': 3, 'High': 4, 'Very High': 5},
    'anxiety_frequency': {'Never': 5, 'Rarely': 4, 'Sometimes': 3, 'Often': 2, 'Almost Always': 1},
    'self_worth': {'Very Negative': 1, 'Negative': 2, 'Neutral': 3, 'Positive': 4, 'Very Positive': 5}
}


MAX_SCORE = 50


score_ranges = {
    'Excellent': (40, 50),    
    'Good': (30, 39),         
    'Fair': (20, 29),         
    'Poor': (10, 19),         
    'Critical': (0, 9)        
}
