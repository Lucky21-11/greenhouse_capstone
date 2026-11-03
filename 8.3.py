#ARYAN SHARMA 16015025070
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Age": [20, 21, np.nan, 22, 19, np.nan, 20, 21, 22, 20],
    "Temperature": [98.2, np.nan, 99.1, 98.6, 100.2, 99.0, np.nan, 98.4, 99.5, 98.8],
    "BP": [120, 125, 118, np.nan, 130, 122, 119, np.nan, 128, 121],
    "Status": ["Normal", "Normal", np.nan, "Normal", "High",
               "Normal", "Normal", "High", np.nan, "Normal"]
})

print("Missing Values:")
print(df.isnull().sum())

print("\nMissing Percentage:")
print(df.isnull().mean() * 100)

drop_df = df.dropna()

fill_df = df.copy()

for col in ["Age", "Temperature", "BP"]:
    fill_df[col] = fill_df[col].fillna(fill_df[col].mean())

fill_df["Status"] = fill_df["Status"].fillna(fill_df["Status"].mode()[0])

print("\nRows after dropna:", len(drop_df))
print("Rows after fillna:", len(fill_df))


print("\nData after fillna:")
print(fill_df)