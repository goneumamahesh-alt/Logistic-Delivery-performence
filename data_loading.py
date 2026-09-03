"""
data_loading.py

Week 1 prototype script: load the logistics dataset and print a basic
structural overview. Update DATA_PATH and column names to match the
dataset you selected from data/README.md.
"""

import pandas as pd

DATA_PATH = "data/logistics_data.csv"


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the logistics dataset from a CSV file."""
    df = pd.read_csv(path)
    return df


def summarize(df: pd.DataFrame) -> None:
    """Print a quick structural summary of the dataset."""
    print("First 5 rows:")
    print(df.head())
    print("\nDataset info:")
    print(df.info())
    print("\nShape (rows, columns):", df.shape)


if __name__ == "__main__":
    data = load_data()
    summarize(data)
