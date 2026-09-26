import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
data = pd.read_csv(PROJECT_DIR / "data" / "us-states.csv")
data["date"] = pd.to_datetime(data["date"])


### Visualization of Daily New Cases
def plot_daily_cases(states):
    data_sorted = data.sort_values(["state", "date"]).copy()
    data_sorted["daily_cases"] = data_sorted.groupby("state")["cases"].diff()

    plt.figure(figsize=(12, 6))

    for state in states:
        state_data = data_sorted[data_sorted["state"] == state]

        plt.plot(
            state_data["date"],
            state_data["daily_cases"],
            label=state,
        )

    plt.title("Daily New COVID-19 Cases in Coastal States")
    plt.xlabel("Date")
    plt.ylabel("Daily New Cases")
    plt.legend()
    plt.tight_layout()
    output_path = PROJECT_DIR / "figures" / "daily_cases_comparison.png"
    plt.savefig(output_path, dpi=300)
    plt.close()
    return output_path


### Identify Peak Case Dates
def find_peak_date(state):
    data_sorted = data.sort_values(["state", "date"]).copy()
    data_sorted["daily_cases"] = data_sorted.groupby("state")["cases"].diff()

    state_data = data_sorted[data_sorted["state"] == state]
    peak_index = state_data["daily_cases"].idxmax()

    return state_data.loc[peak_index, "date"]

california_peak_date = find_peak_date("California")

### Compare Peak Dates Between States
def compare_peak_dates(state_one, state_two):
    peak_date_one = find_peak_date(state_one)
    peak_date_two = find_peak_date(state_two)

    days_between = abs((peak_date_one - peak_date_two).days)

    if peak_date_one < peak_date_two:
        first_state = state_one
    elif peak_date_two < peak_date_one:
        first_state = state_two
    else:
        first_state = "Both states"

    return first_state, days_between
print("California peak date:", california_peak_date.date())

first_state, days_between = compare_peak_dates("California", "New York")
print(
    f"{first_state} reached its peak "
    f"{days_between} days before the other state."
)

### Data Exploration & Anomaly Analysis
florida_data = data[data["state"] == "Florida"].sort_values("date").copy()
florida_data["daily_cases"] = florida_data["cases"].diff()

florida_anomalies = florida_data[florida_data["daily_cases"] < 0]

print(
    "Florida days with negative daily cases:\n",
    florida_anomalies[["date", "daily_cases"]]
)

figure_path = plot_daily_cases(["California", "Florida", "New York"])
print("Saved figure:", figure_path)
