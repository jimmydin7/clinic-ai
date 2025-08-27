def bmi_class(bmi: float) -> tuple[str, str]:
    if bmi < 16:
        return "Underweight (Severe)", "Orange"
    elif bmi < 17:
        return "Underweight (Moderate)", "Orange"
    elif bmi < 18.5:
        return "Underweight (Mild)", "Orange"
    elif bmi < 21:
        return "Normal weight (Low-normal)", "Green"
    elif bmi < 23.5:
        return "Normal weight (Mid-normal)", "Green"
    elif bmi < 25:
        return "Normal weight (High-normal)", "Green"
    elif bmi < 30:
        return "Overweight (Pre-obese)", "Red"
    elif bmi < 35:
        return "Obese (Class I)", "Red"
    elif bmi < 40:
        return "Obese (Class II)", "Red"
    else:
        return "Obese (Class III)", "Red"