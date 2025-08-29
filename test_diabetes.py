from models.diabetes.diabetes import predict_diabetes

test_data = {
    'Age': 45,
    'Pregnancies': 2,
    'Glucose': 140,
    'BloodPressure': 135,
    'SkinThickness': 25,
    'Insulin': 150,
    'BMI': 32,
    'DiabetesPedigreeFunction': 0.9
}

result = predict_diabetes(test_data)
print(f"Test Data: {test_data}")
print(f"Predicted Risk: {result}%")

if result >= 70:
    print("Risk Level: High")
elif result >= 50:
    print("Risk Level: Medium")
else:
    print("Risk Level: Low")
