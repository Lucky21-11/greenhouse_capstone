import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

df = pd.read_csv("robotics.csv")
df.columns = df.columns.str.strip().str.lower()

print(df.head())


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="load", y="temperature",
                size="power", hue="vibration", sizes=(40, 300),
                palette="viridis")
plt.title("Load vs Temperature")
plt.xlabel("Load")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("q3_scatterplot.png")
plt.show()


plt.figure(figsize=(8, 6))
sns.regplot(data=df, x="load", y="temperature",
            scatter_kws={"s": 60, "alpha": 0.7})
plt.title("Load vs Temperature (Regression)")
plt.xlabel("Load")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("q3_regplot.png")
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(data=df, x="temperature", bins=8, kde=True)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("q3_histplot.png")
plt.show()


g = sns.jointplot(data=df, x="load", y="temperature", kind="reg", height=6)
g.fig.suptitle("Load vs Temperature")
g.set_axis_labels("Load", "Temperature")
g.savefig("q3_jointplot.png")
plt.show()


corr = df["load"].corr(df["temperature"])

print("\nCorrelation:", round(corr, 3))
print("Temperature increases as motor load increases.")