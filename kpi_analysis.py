"""
kpi_analysis.py

Week 1 prototype script: calculates the six core logistics KPIs defined in
the strategic planning report.
"""

from data_loading import load_data
from data_cleaning import clean_data


def on_time_delivery_rate(df) -> float:
    return (df["is_delayed"] == False).sum() / len(df) * 100  # noqa: E712


def average_delivery_time(df) -> float:
    return df["delivery_time"].mean()


def delivery_delay_rate(df) -> float:
    return (df["is_delayed"] == True).sum() / len(df) * 100  # noqa: E712


def average_delivery_distance(df) -> float:
    return df["distance_km"].mean()


def cost_per_delivery(df) -> float:
    return df["delivery_cost"].sum() / len(df)


def vehicle_utilization_rate(df):
    loaded = df.groupby("vehicle_id")["order_quantity"].sum()
    capacity = df.groupby("vehicle_id")["vehicle_capacity"].first()
    return (loaded / capacity) * 100


def calculate_all_kpis(df) -> dict:
    kpis = {
        "on_time_delivery_rate_pct": on_time_delivery_rate(df),
        "average_delivery_time_days": average_delivery_time(df),
        "delivery_delay_rate_pct": delivery_delay_rate(df),
        "average_delivery_distance_km": average_delivery_distance(df),
        "cost_per_delivery": cost_per_delivery(df),
        "average_vehicle_utilization_pct": vehicle_utilization_rate(df).mean(),
    }
    return kpis


if __name__ == "__main__":
    raw_data = load_data()
    cleaned = clean_data(raw_data)
    results = calculate_all_kpis(cleaned)

    print("\nLogistics KPI Summary")
    print("-" * 40)
    for name, value in results.items():
        print(f"{name}: {value:.2f}")
