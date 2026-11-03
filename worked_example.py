
import pandas as pd

df = pd.read_csv(
    "g6_irrigation_data_fixed.csv",
    keep_default_na=False
)

sample = df[
    (df["date"] >= "2022-05-03") &
    (df["date"] <= "2022-05-22")
].copy()

given = (
    (sample["soil_cat"] == "Dry") &
    (sample["rain_cat"] == "None")
)

event = given & (sample["soil_next_dry"] == "1")

n = int(given.sum())
event_count = int(event.sum())

print(sample[[
    "date", "rain_cat", "soil_cat", "soil_next_dry"
]].to_string(index=False))

print("Sample size:", len(sample))
print("Condition count:", n)
print("Dry tomorrow count:", event_count)

if n > 0:
    print("Conditional probability:", event_count / n)
else:
    print("Conditional probability is undefined")

