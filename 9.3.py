import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("flights.csv")

pivot_data = df.pivot(
    index="month",
    columns="year",
    values="passengers"
)

plt.figure(figsize=(12, 7))

plt.contourf(
    pivot_data.columns,
    range(len(pivot_data.index)),
    pivot_data.values,
    cmap="viridis"
)

plt.colorbar(label="Number of Passengers")

plt.yticks(
    range(len(pivot_data.index)),
    pivot_data.index
)

plt.xlabel("Year")
plt.ylabel("Month")
plt.title("Seasonal Airline Passenger Trends")

plt.show()