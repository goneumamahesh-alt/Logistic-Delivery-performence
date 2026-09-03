"""
eda.py

Week 1 prototype script: exploratory data analysis visualizations for the
logistics dataset — delivery status distribution, delivery time distribution,
distance vs. delivery time, and cost by vehicle type.
"""

import matplotlib.pyplot as plt
import seaborn as sns

from data_loading import load_data
from data_cleaning import clean_data


def plot_delivery_status_distribution(df):
    sns.countplot(x="delivery_status", data=df)
    plt.title("Delivery Status Distribution")
    plt.xlabel("Delivery Status")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("delivery_status_distribution.png")
    plt.close()


def plot_delivery_time_distribution(df):
    sns.histplot(df["delivery_time"], bins=20, kde=True)
    plt.title("Delivery Time Distribution")
    plt.xlabel("Delivery Time (days)")
    plt.tight_layout()
    plt.savefig("delivery_time_distribution.png")
    plt.close()


def plot_distance_vs_delivery_time(df):
    sns.scatterplot(x="distance_km", y="delivery_time", data=df)
    plt.title("Distance vs Delivery Time")
    plt.xlabel("Distance (km)")
    plt.ylabel("Delivery Time (days)")
    plt.tight_layout()
    plt.savefig("distance_vs_delivery_time.png")
    plt.close()


def plot_cost_by_vehicle_type(df):
    sns.boxplot(x="vehicle_type", y="delivery_cost", data=df)
    plt.title("Delivery Cost by Vehicle Type")
    plt.xlabel("Vehicle Type")
    plt.ylabel("Delivery Cost")
    plt.tight_layout()
    plt.savefig("cost_by_vehicle_type.png")
    plt.close()


def run_eda(df):
    print("Correlation matrix (numeric columns):")
    print(df.corr(numeric_only=True))
    plot_delivery_status_distribution(df)
    plot_delivery_time_distribution(df)
    plot_distance_vs_delivery_time(df)
    plot_cost_by_vehicle_type(df)
    print("EDA charts saved as PNG files in the current directory.")


if __name__ == "__main__":
    raw_data = load_data()
    cleaned = clean_data(raw_data)
    run_eda(cleaned)
