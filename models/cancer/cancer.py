import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def load_dataset():
    dataset_path = Path(__file__).resolve().parents[2] / "datasets" / "cancer.csv"
    return pd.read_csv(dataset_path)

df = load_dataset()


