#ARYAN SHARMA 16015025070
import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Mouse", "Keyboard",
                "Monitor", "Headphones", "Printer", "Laptop", "Phone",
                "Tablet", "Mouse", "Monitor", "Printer", "Keyboard"],
    "Region": ["East", "West", "East", "North", "South",
               "East", "West", "North", "South", "East",
               "West", "North", "South", "East", "West"],
    "Quantity": [10, 5, 8, 20, 15, 6, 12, 7, 9, 10, 5, 25, 8, 6, 12],
    "Price": [700, 1200, 800, 300, 400, 1500, 600, 900, 700, 1000,
              900, 250, 1400, 1100, 350]
})

df["Revenue"] = df["Quantity"] * df["Price"]

result = df[(df["Region"] == "East") & (df["Revenue"] > 5000)]
print("East Region and Revenue > 5000:")
print(result)

group = df.groupby("Region")["Revenue"].agg(["sum", "mean"])
print("\nRevenue by Region:")
print(group)

top_region = group["sum"].idxmax()
print("\nTop Performing Region:", top_region)

print("\nUsing loc:")
print(df.loc[0:2, ["Product", "Region", "Revenue"]])

print("\nUsing iloc:")
print(df.iloc[0:3, [0, 1, 4]])