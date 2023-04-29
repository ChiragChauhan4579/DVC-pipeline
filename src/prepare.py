from pathlib import Path
import pandas as pd

def main(repo_path):
    data_path = repo_path / "data"
    train_path = data_path / "raw"
    test_path = data_path / "raw"

    train_df = pd.read_csv(train_path / "train.csv")
    test_df = pd.read_csv(test_path / "test.csv")

    train_df.drop(columns=["id"], inplace=True)
    test_df.drop(columns=["id"], inplace=True)
    train_df.rename(columns={"M": 0,"B":1}, inplace=True)
    test_df.rename(columns={"M": 0,"B":1}, inplace=True)

    prepared = data_path / "prepared"

    train_df.to_csv(prepared / "train.csv", index=False)
    test_df.to_csv(prepared / "test.csv", index=False)

if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    main(repo_path)
