#ARYAN SHARMA 16015025070
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Aryan", "Rahul", "Anish", "Rohan", "Aman", "Karan", "Yash", "Aditya"],
    "Branch": ["CSBS", "CSE", "IT", "CSBS", "CSE", "IT", "CSBS", "CSE"],
    "Age": [19, 20, 19, 20, 19, 21, 20, 19],
    "CGPA": [8.2, 7.1, 9.0, 6.8, 7.8, 8.5, 7.2, 9.1]
})

df["Status"] = np.where(df["CGPA"] >= 7.5, "Eligible", "Not Eligible")

df.loc[8] = ["Vivek", "IT", 20, 8.0, "Eligible"]
df.loc[9] = ["Sahil", "CSBS", 19, 7.0, "Not Eligible"]

df = df.drop(2)

print("Sorted DataFrame:")
print(df.sort_values("CGPA", ascending=False))

print("\nSummary Statistics:")
print(df.describe())