#ARYAN SHARMA 16015025070
import pandas as pd

df = pd.read_csv("geofenced_plots.csv")

print("First 5 Records:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Information:")
df.info()

print("\nStatistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

mean_soil = df["Soil_Moisture"].mean()
df["Soil_Moisture"] = df["Soil_Moisture"].fillna(mean_soil)

print("\nMissing Soil Moisture After Filling:")
print(df["Soil_Moisture"].isnull().sum())

print("\nPlots with Soil Moisture Below 40%:")
print(df[df["Soil_Moisture"] < 40])

print("\nAverage Irrigation Duration by Crop:")
crop_irrigation = df.groupby("Crop_Variety")["Irrigation_Duration"].mean()
print(crop_irrigation)

print("\nFarmer-Wise Analysis:")
farmer_analysis = df.groupby("Farmer_Name")["Irrigation_Duration"].agg(
    ["count", "mean"]
)
print(farmer_analysis)

print("\nCrop-Wise Soil Moisture Analysis:")
soil_analysis = df.groupby("Crop_Variety")["Soil_Moisture"].agg(
    ["mean", "min", "max"]
)
print(soil_analysis)

top_crop = crop_irrigation.idxmax()
top_duration = crop_irrigation.max()

print("\nCrop Variety Requiring Maximum Average Irrigation:")
print(top_crop)

print("Average Irrigation Duration:", top_duration, "minutes")

print("\nFinal Crop Analysis:")
final_analysis = df.groupby("Crop_Variety").agg(
    Average_Irrigation=("Irrigation_Duration", "mean"),
    Average_Soil_Moisture=("Soil_Moisture", "mean"),
    Minimum_Soil_Moisture=("Soil_Moisture", "min"),
    Maximum_Soil_Moisture=("Soil_Moisture", "max")
)

print(final_analysis)