
import pandas as pd
from probability import (
    joint_prob,
    marginal_prob,
    conditional_prob
)

df = pd.read_csv(
    "g6_irrigation_data_fixed.csv",
    keep_default_na=False
)

df["soil_next_dry"] = pd.to_numeric(
    df["soil_next_dry"]
)

print("Joint:", joint_prob(df, "Dry", "None"))

print("Marginal:", marginal_prob(
    df, "soil_cat", "Dry"
))

print("Conditional:", conditional_prob(
    df,
    {"soil_next_dry": 1},
    {"soil_cat": "Dry", "rain_cat": "None"}
))
