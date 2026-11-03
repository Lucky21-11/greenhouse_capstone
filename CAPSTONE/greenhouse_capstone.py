

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

# 1. Read the CSV file
def load_data():
    data = pd.read_csv("texcoco_greenhouse_enriched_1week_top30.csv")
    print("Dataset Shape:", data.shape)
    print("\nFirst 5 Rows:")
    print(data.head())
    return data


# 2. Clean the data
def clean_data(data):
    # Convert timestamp into date and time format
    data["timestamp_local"] = pd.to_datetime(
        data["timestamp_local"], dayfirst=True, errors="coerce"
    )

    # Remove rows where timestamp is missing
    data = data.dropna(subset=["timestamp_local"])

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Convert measurement columns to numbers
    for column in data.columns:
        if column not in ["timestamp_local", "fecha", "hora"]:
            data[column] = pd.to_numeric(data[column], errors="coerce")

    # Fill missing numeric values with the column average
    for column in data.select_dtypes(include="number").columns:
        data[column] = data[column].fillna(data[column].mean())

    data = data.sort_values("timestamp_local")
    data = data.reset_index(drop=True)

    print("\nMissing Values After Cleaning:")
    print(data.isnull().sum().sum())

    return data


#  Analyze the dataset
def analyze_data(data):
    print("\nDataset Information:")
    data.info()

    print("\nStatistical Summary:")
    print(data.describe())

    moisture = data["hum_suelo"]

    print("\nSoil Moisture Analysis")
    print("Average:", round(moisture.mean(), 2), "%")
    print("Minimum:", round(moisture.min(), 2), "%")
    print("Maximum:", round(moisture.max(), 2), "%")

    # Use 30% as an example threshold for this demonstration.
    # The correct threshold depends on the crop and sensor.
    low_moisture = data[data["hum_suelo"] < 30]
    print("Readings below 30%:", len(low_moisture))

    return data


def draw_graphs(data):
    # Line graph: soil moisture over time
    plt.figure(figsize=(10, 4))
    plt.plot(data["timestamp_local"], data["hum_suelo"])
    plt.title("Soil Moisture Over Time")
    plt.xlabel("Date and Time")
    plt.ylabel("Soil Moisture (%)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("soil_moisture_line.png")
    plt.show()

    # Scatter plot: air temperature and soil moisture
    plt.figure(figsize=(7, 4))
    sns.scatterplot(data=data, x="temp_aire_media", y="hum_suelo")
    plt.title("Air Temperature vs Soil Moisture")
    plt.xlabel("Air Temperature")
    plt.ylabel("Soil Moisture (%)")
    plt.tight_layout()
    plt.savefig("temperature_scatter.png")
    plt.show()

    # Histogram: soil moisture distribution
    plt.figure(figsize=(7, 4))
    plt.hist(data["hum_suelo"], bins=20, edgecolor="black")
    plt.title("Soil Moisture Distribution")
    plt.xlabel("Soil Moisture (%)")
    plt.ylabel("Number of Readings")
    plt.tight_layout()
    plt.savefig("soil_moisture_histogram.png")
    plt.show()

    # Heatmap: relationships between numeric variables
    columns = [
        "temp_aire_media",
        "hum_aire_media",
        "temp_suelo",
        "hum_suelo",
        "vpd_media",
        "lux"
    ]

    # Keep only columns that exist in the CSV
    columns = [column for column in columns if column in data.columns]
    correlation = data[columns].corr()

    plt.figure(figsize=(8, 5))
    sns.heatmap(correlation, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.show()


#  Forecast soil moisture using ARIMA
def forecast_moisture(data):
    # Set timestamp as the index
    series = data.set_index("timestamp_local")["hum_suelo"]

    # Convert readings to regular 5-minute intervals
    series = series.resample("5min").mean()
    series = series.interpolate().dropna()

    # Use first 80% for training and last 20% for testing
    split = int(len(series) * 0.8)
    train = series.iloc[:split]
    test = series.iloc[split:]

    if len(train) < 20 or len(test) < 5:
        print("\nNot enough data to build the forecasting model.")
        return

    # ARIMA uses previous values to forecast future values
    model = ARIMA(train, order=(1, 1, 1))
    model_fit = model.fit()

    predictions = model_fit.forecast(steps=len(test))

    # Calculate forecasting errors
    actual = test.to_numpy()
    predicted = np.array(predictions)

    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))

    print("\nForecasting Results")
    print("Mean Absolute Error:", round(mae, 2))
    print("Root Mean Squared Error:", round(rmse, 2))

    # Show actual values and predicted values
    plt.figure(figsize=(10, 4))
    plt.plot(test.index, actual, label="Actual")
    plt.plot(test.index, predicted, label="Predicted")
    plt.title("Actual vs Predicted Soil Moisture")
    plt.xlabel("Date and Time")
    plt.ylabel("Soil Moisture (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("soil_moisture_forecast.png")
    plt.show()

    # Simple irrigation warning based on predicted moisture
    if predicted[-1] < 30:
        print("Warning: Predicted soil moisture is below 30%. Check irrigation.")
    else:
        print("Predicted soil moisture is not below the example 30% threshold.")


# 6. Main function
def main():
    data = load_data()
    data = clean_data(data)
    analyze_data(data)
    draw_graphs(data)
    forecast_moisture(data)

    # Save the cleaned data
    data.to_csv("cleaned_greenhouse_data.csv", index=False)
    print("\nCleaned data saved successfully.")
    print("Project completed.")


main()
