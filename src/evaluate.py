from joblib import load
import json
from pathlib import Path
import pandas as pd
from sklearn.metrics import accuracy_score

def main(repo_path):
    test_df = pd.read_csv(repo_path / "data/prepared/test.csv")
    labels = test_df["diagnosis"]
    test_df = test_df.drop("diagnosis", axis=1)
    model = load(repo_path / "model/model.joblib")
    predictions = model.predict(test_df)
    accuracy = accuracy_score(labels, predictions)
    metrics = {"accuracy": accuracy}
    accuracy_path = repo_path / "metrics/accuracy.json"
    accuracy_path.write_text(json.dumps(metrics))

if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    main(repo_path)
