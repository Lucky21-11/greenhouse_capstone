import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv("flights.csv")
mpg = pd.read_csv("mpg.csv")

yearly_passengers = flights.groupby("year")["passengers"].sum()
average_passengers = yearly_passengers.mean()

plt.figure(figsize=(10, 5))
plt.plot(
    yearly_passengers.index,
    yearly_passengers.values,
    marker="o",
    label="Total Passengers"
)
plt.fill_between(
    yearly_passengers.index,
    yearly_passengers.values,
    average_passengers,
    alpha=0.3,
    label="Deviation from Average"
)
plt.axhline(
    average_passengers,
    linestyle="--",
    label="Overall Average"
)
plt.title("Yearly Airline Passenger Trend")
plt.xlabel("Year")
plt.ylabel("Total Passengers")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    mpg["horsepower"],
    mpg["mpg"],
    c=mpg["model_year"],
    cmap="viridis"
)
plt.colorbar(scatter, label="Model Year")
plt.title("Horsepower vs MPG")
plt.xlabel("Horsepower")
plt.ylabel("Miles Per Gallon")
plt.show()