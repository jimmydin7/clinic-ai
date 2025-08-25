import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def load_dataset():
    dataset_path = Path(__file__).resolve().parents[2] / "datasets" / "cancer.csv"
    return pd.read_csv(dataset_path)

df = load_dataset()


X = df.drop('Diagnosis', axis=1)

Y = df['Diagnosis']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, Y_train)

