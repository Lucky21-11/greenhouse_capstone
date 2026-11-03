#ARYAN SHARMA 16015025070
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

crop_data = {
    "Crop Cycle Day": [0, 15, 30, 45, 60, 75, 90, 105, 120],
    "Crop Stage": [
        "Germination", "Germination",
        "Tillering", "Tillering",
        "Grand Growth", "Grand Growth", "Grand Growth",
        "Maturity", "Maturity"
    ],
    "Soil Moisture (%)": [68, 63, 57, 51, 44, 39, 35, 42, 50]
}

df = pd.DataFrame(crop_data)

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df,
    x="Crop Cycle Day",
    y="Soil Moisture (%)",
    hue="Crop Stage",
    marker="o",
    linewidth=2
)

plt.axhline(y=40, color="red", linestyle="--", label="Critical Moisture Level")
min_point = df.loc[df["Soil Moisture (%)"].idxmin()]

plt.scatter(
    min_point["Crop Cycle Day"],
    min_point["Soil Moisture (%)"],
    color="black",
    s=100,
    zorder=5,
    label="Minimum Moisture"
)

plt.title("Soil Moisture Variation During Crop Cycle")
plt.xlabel("Crop Cycle Day")
plt.ylabel("Soil Moisture (%)")
plt.legend()
plt.tight_layout()
plt.show()

water_stress = {
    "R1": [22, 28, 18, 32],
    "R2": [35, 42, 31, 46],
    "R3": [48, 55, 51, 63],
    "R4": [61, 67, 73, 69],
    "R5": [30, 36, 44, 41]
}

regions = ["North", "South", "East", "West"]
stress_df = pd.DataFrame(water_stress, index=regions)

plt.figure(figsize=(9, 6))
sns.heatmap(
    stress_df,
    annot=True,
    fmt="d",
    cmap="coolwarm",
    linewidths=0.5,
    cbar_kws={"label": "Water Stress Index (WSI)"}
)

plt.title("Regional Water Stress Heat Map")
plt.xlabel("Region Zone")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

max_value = stress_df.max().max()
max_location = stress_df.stack().idxmax()
severe_cells = (stress_df >= 70).sum().sum()

print("Region with Highest Water Stress:", max_location[0])
print("Corresponding Zone:", max_location[1])
print("Maximum WSI Value:", max_value)
print("Number of Cells with WSI >= 70:", severe_cells)

print("\nAverage WSI for Each Region:")
print(stress_df.mean(axis=1))

if df["Soil Moisture (%)"].min() < 40:
    print("\nThe plot requires irrigation during the later crop stages.")
else:
    print("\nThe plot does not require irrigation.")