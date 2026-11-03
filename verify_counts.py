
import pandas as pd

df = pd.read_csv(
    "g6_irrigation_data_fixed.csv",
    keep_default_na=False
)

df["soil_next_dry"] = pd.to_numeric(df["soil_next_dry"])

N = len(df)

# 1. Joint probability: Dry soil AND None rainfall
joint_count = (
    (df["soil_cat"] == "Dry") &
    (df["rain_cat"] == "None")
).sum()

joint_probability = joint_count / N

# 2. Marginal probability: Dry soil
dry_count = (df["soil_cat"] == "Dry").sum()
marginal_probability = dry_count / N

# 3. Conditional probability: Dry tomorrow given Dry soil and None rainfall
condition = (
    (df["soil_cat"] == "Dry") &
    (df["rain_cat"] == "None")
)

denominator = condition.sum()

event_count = (
    condition & (df["soil_next_dry"] == 1)
).sum()

conditional_probability = event_count / denominator

print("Total rows:", N)
print("Joint:", joint_count, "/", N, "=", round(joint_probability, 4))
print("Marginal:", dry_count, "/", N, "=", round(marginal_probability, 4))
print(
    "Conditional:",
    event_count, "/", denominator,
    "=", round(conditional_probability, 4)
)

