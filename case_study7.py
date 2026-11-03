#ARYAN SHARMA 16015025070
import numpy as np

soil_moisture = np.array([42.5, 35.0, 28.5, 51.0, 32.0])
plot_ids = np.array(["P101", "P102", "P103", "P104", "P105"])

threshold = 40

stress_flag = soil_moisture < threshold

stressed_plots = plot_ids[stress_flag]
stressed_moisture = soil_moisture[stress_flag]

total_stressed = np.sum(stress_flag)
percentage = (total_stressed / len(plot_ids)) * 100

print("Soil Moisture Array:", soil_moisture)
print("Water Stress Flags:", stress_flag)
print("Water-Stressed Plots:", stressed_plots)
print("Soil Moisture of Stressed Plots:", stressed_moisture)
print("Total Water-Stressed Plots:", total_stressed)
print("Total Plots:", len(plot_ids))
print("Water-Stressed Percentage:", percentage, "%")