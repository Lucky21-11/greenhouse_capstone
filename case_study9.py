import numpy as np
import matplotlib.pyplot as plt

days = [0, 15, 30, 45, 60, 75, 90, 105, 120]
soil_moisture = [65, 60, 55, 48, 42, 38, 45, 52, 58]

threshold = 40

min_moisture = min(soil_moisture)
min_day = days[soil_moisture.index(min_moisture)]

plt.figure(figsize=(10, 6))

plt.plot(
    days,
    soil_moisture,
    marker="o",
    label="Soil Moisture"
)

plt.axhline(
    threshold,
    linestyle="--",
    label="Water Stress Threshold (40%)"
)

plt.annotate(
    f"Minimum: {min_moisture}% on Day {min_day}",
    xy=(min_day, min_moisture),
    xytext=(min_day + 10, min_moisture - 8),
    arrowprops=dict(arrowstyle="->")
)

plt.title("Soil Moisture Variation During Crop Cycle")
plt.xlabel("Crop Cycle (Days)")
plt.ylabel("Soil Moisture (%)")
plt.grid(True)
plt.legend()
plt.show()


water_stress = np.array([
    [20, 35, 45, 60, 30],
    [25, 40, 55, 65, 35],
    [15, 30, 50, 70, 45],
    [30, 45, 60, 75, 40]
])

plt.figure(figsize=(9, 6))

heatmap = plt.imshow(
    water_stress,
    cmap="YlOrRd"
)

plt.colorbar(heatmap, label="Water-Stress Index")

plt.title("Regional Water-Stress Heat Map")
plt.xlabel("Region Column")
plt.ylabel("Region Row")

for i in range(water_stress.shape[0]):
    for j in range(water_stress.shape[1]):
        plt.text(
            j,
            i,
            water_stress[i, j],
            ha="center",
            va="center"
        )

plt.show()


max_value = np.max(water_stress)

position = np.unravel_index(
    np.argmax(water_stress),
    water_stress.shape
)

row = position[0] + 1
column = position[1] + 1

print("Maximum Water Stress :", max_value)
print("Region : Row", row, ", Column", column)
print("Status : Severe Water Stress")