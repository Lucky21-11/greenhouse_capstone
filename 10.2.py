#ARYAN SHARMA 16015025070
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("diamonds.csv")

sample_df = df.sample(500, random_state=1)

plt.figure(figsize=(8, 6))
sns.regplot(x="carat", y="price", data=sample_df)
plt.title("Carat vs Price - Regression Plot")
plt.xlabel("Carat")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

sns.jointplot(x="carat", y="price", data=df, kind="hex")
plt.suptitle("Carat vs Price - Hex Joint Plot", y=1.02)
plt.show()