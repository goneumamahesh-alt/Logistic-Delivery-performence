"""
data_cleaning.py

Week 1 prototype script: basic cleaning steps for the logistics dataset —
missing-value check, duplicate check, date parsing, and derived fields
(delivery_time, is_delayed). Adjust column names to match your dataset.
"""

import pandas as pd

from data_loading import load_data


def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """Return a count of missing values per column."""
    missing = df.isnull().sum()
    print("Missing values per column:")
    print(missing)
    return missing


def check_duplicates(df: pd.DataFrame) -> int:
    """Return the number of duplicate rows."""
    duplicate_count = df.duplicated().sum()
    print(f"Duplicate rows: {duplicate_count}")
    return duplicate_count


def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Convert order and delivery date columns to datetime."""
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["delivery_date"] = pd.to_datetime(df["delivery_date"])
    df["expected_delivery_date"] = pd.to_datetime(df["expected_delivery_date"])
    return df


def add_derived_fields(df: pd.DataFrame) -> pd.DataFrame:
    """Add delivery_time (days) and is_delayed (bool) derived columns."""
    df["delivery_time"] = (df["delivery_date"] - df["order_date"]).dt.days
    df["is_delayed"] = df["delivery_date"] > df["expected_delivery_date"]
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Run the full Week 1 cleaning pipeline."""
    check_missing_values(df)
    check_duplicates(df)
    df = df.drop_duplicates()
    df = parse_dates(df)
    df = add_derived_fields(df)
    return df


if __name__ == "__main__":
    raw_data = load_data()
    cleaned = clean_data(raw_data)
    print("\nCleaned dataset preview:")
    print(cleaned.head())
