
import pandas as pd
from probability import dry_tomorrow_by_soil

df = pd.read_csv(
    "g6_irrigation_data_fixed.csv",
    keep_default_na=False
)

df["soil_next_dry"] = pd.to_numeric(df["soil_next_dry"])

print(dry_tomorrow_by_soil(df).to_string(index=False))

