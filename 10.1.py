#ARYAN SHARMA 16015025070
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("penguins.csv")
df.dropna(subset=["species", "island", "body_mass_g", "flipper_length_mm"], inplace=True)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.boxplot(x="species", y="body_mass_g", data=df, ax=axes[0, 0])
axes[0, 0].set_title("Body Mass by Species - Boxplot")
axes[0, 0].set_xlabel("Species")
axes[0, 0].set_ylabel("Body Mass (g)")

sns.violinplot(x="species", y="body_mass_g", data=df, ax=axes[0, 1])
axes[0, 1].set_title("Body Mass by Species - Violinplot")
axes[0, 1].set_xlabel("Species")
axes[0, 1].set_ylabel("Body Mass (g)")

sns.boxplot(x="species", y="flipper_length_mm", data=df, ax=axes[1, 0])
sns.swarmplot(x="species", y="flipper_length_mm", data=df, ax=axes[1, 0], size=3)
axes[1, 0].set_title("Flipper Length by Species")
axes[1, 0].set_xlabel("Species")
axes[1, 0].set_ylabel("Flipper Length (mm)")

sns.countplot(x="species", hue="island", data=df, ax=axes[1, 1])
axes[1, 1].set_title("Penguin Count by Species and Island")
axes[1, 1].set_xlabel("Species")
axes[1, 1].set_ylabel("Number of Penguins")
axes[1, 1].legend(title="Island")

plt.tight_layout()
plt.show()