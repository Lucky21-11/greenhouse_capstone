import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

def load_data():
    data = pd.read_csv("texcoco_greenhouse_enriched_1week_top30 2.csv")
    print("Dataset Shape:", data.shape)
    print("\nFirst 5 Rows:")
    print(data.head())
    return data


def clean_data(data):
    data["timestamp_local"] = pd.to_datetime(
        data["timestamp_local"], dayfirst=True, errors="coerce"
    )

    data = data.dropna(subset=["timestamp_local"])
    data = data.drop_duplicates()

    for column in data.columns:
        if column not in ["timestamp_local", "fecha", "hora"]:
            data[column] = pd.to_numeric(data[column], errors="coerce")

    for column in data.select_dtypes(include="number").columns:
        data[column] = data[column].fillna(data[column].mean())

    data = data.sort_values("timestamp_local")
    data = data.reset_index(drop=True)

    print("\nMissing Values After Cleaning:")
    print(data.isnull().sum().sum())

    return data


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

    low_moisture = data[data["hum_suelo"] < 30]
    print("Readings below 30%:", len(low_moisture))

    return data


def draw_graphs(data):
    # Soil moisture over time
    plt.figure(figsize=(10, 4))
    plt.plot(data["timestamp_local"], data["hum_suelo"])
    plt.title("Soil Moisture Over Time")
    plt.xlabel("Date and Time")
    plt.ylabel("Soil Moisture (%)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("soil_moisture_line.png")
    plt.show()

    # Air temperature vs soil moisture
    plt.figure(figsize=(7, 4))
    sns.scatterplot(data=data, x="temp_aire_media", y="hum_suelo")
    plt.title("Air Temperature vs Soil Moisture")
    plt.xlabel("Air Temperature")
    plt.ylabel("Soil Moisture (%)")
    plt.tight_layout()
    plt.savefig("temperature_scatter.png")
    plt.show()

    # Soil moisture distribution
    plt.figure(figsize=(7, 4))
    plt.hist(data["hum_suelo"], bins=20, edgecolor="black")
    plt.title("Soil Moisture Distribution")
    plt.xlabel("Soil Moisture (%)")
    plt.ylabel("Number of Readings")
    plt.tight_layout()
    plt.savefig("soil_moisture_histogram.png")
    plt.show()

    columns = [
        "temp_aire_media",
        "hum_aire_media",
        "temp_suelo",
        "hum_suelo",
        "vpd_media",
        "lux"
    ]

    columns = [column for column in columns if column in data.columns]
    correlation = data[columns].corr()
    
     #Correlation heatmap
    plt.figure(figsize=(8, 5))
    sns.heatmap(correlation, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.show()


def forecast_moisture(data):
    series = data.set_index("timestamp_local")["hum_suelo"]

    series = series.resample("5min").mean()
    series = series.interpolate().dropna()

    split = int(len(series) * 0.8)
    train = series.iloc[:split]
    test = series.iloc[split:]

    if len(train) < 20 or len(test) < 5:
        print("\nNot enough data to build the forecasting model.")
        return

    model = ARIMA(train, order=(1, 1, 1))
    model_fit = model.fit()

    predictions = model_fit.forecast(steps=len(test))

    actual = test.to_numpy()
    predicted = np.array(predictions)

    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))

    print("\nForecasting Results")
    print("Mean Absolute Error:", round(mae, 2))
    print("Root Mean Squared Error:", round(rmse, 2))

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

    if predicted[-1] < 30:
        print("Warning: Predicted soil moisture is below 30%. Check irrigation.")
    else:
        print("Predicted soil moisture is not below the example 30% threshold.")


def main():
    data = load_data()
    data = clean_data(data)
    analyze_data(data)
    draw_graphs(data)
    forecast_moisture(data)

    data.to_csv("cleaned_greenhouse_data.csv", index=False)
    print("\nCleaned data saved successfully.")
    print("Project completed.")


main()
