import pandas as pd
import numpy as np

def predict_diabetes(data):
    risk_score = 0
    
    age = data['Age']
    pregnancies = data['Pregnancies']
    glucose = data['Glucose']
    blood_pressure = data['BloodPressure']
    skin_thickness = data['SkinThickness']
    insulin = data['Insulin']
    bmi = data['BMI']
    diabetes_pedigree = data['DiabetesPedigreeFunction']
    
    if age > 45:
        risk_score += 2
    elif age > 35:
        risk_score += 1
    
    if pregnancies > 0:
        risk_score += 1
    
    if glucose > 125:
        risk_score += 3
    elif glucose > 100:
        risk_score += 2
    elif glucose > 70:
        risk_score += 0
    else:
        risk_score += 1
    
    if blood_pressure > 130:
        risk_score += 2
    elif blood_pressure > 120:
        risk_score += 1
    
    if bmi > 30:
        risk_score += 2
    elif bmi > 25:
        risk_score += 1
    
    if insulin > 140:
        risk_score += 1
    
    if diabetes_pedigree > 0.8:
        risk_score += 1
    
    max_score = 12
    risk_percentage = (risk_score / max_score) * 100
    
    if risk_percentage >= 70:
        return 85
    elif risk_percentage >= 50:
        return 65
    elif risk_percentage >= 30:
        return 45
    else:
        return 25
