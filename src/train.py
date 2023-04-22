from joblib import dump
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def main(repo_path):
    train_df = pd.read_csv(repo_path / "data/prepared/train.csv")
    X = train_df.drop("diagnosis", axis=1)
    y = train_df["diagnosis"]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)
    dump(model, repo_path / "model/model.joblib")

if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    main(repo_path)
