import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("tips.csv")

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

avg_tip = df.groupby("day")["tip"].mean()
axes[0, 0].bar(avg_tip.index, avg_tip.values)
axes[0, 0].set_title("Average Tip Amount by Day")
axes[0, 0].set_xlabel("Day")
axes[0, 0].set_ylabel("Average Tip")

time_count = df["time"].value_counts()
axes[0, 1].pie(
    time_count.values,
    labels=time_count.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[0, 1].set_title("Lunch vs Dinner Bills")

axes[1, 0].hist(df["total_bill"], bins=15, edgecolor="black")
axes[1, 0].set_title("Total Bill Distribution")
axes[1, 0].set_xlabel("Total Bill")
axes[1, 0].set_ylabel("Frequency")

smoker_tips = df[df["smoker"] == "Yes"]["tip"]
non_smoker_tips = df[df["smoker"] == "No"]["tip"]

axes[1, 1].violinplot(
    [smoker_tips, non_smoker_tips],
    showmeans=True
)
axes[1, 1].set_xticks([1, 2])
axes[1, 1].set_xticklabels(["Smokers", "Non-Smokers"])
axes[1, 1].set_title("Tip Distribution")
axes[1, 1].set_xlabel("Customer Type")
axes[1, 1].set_ylabel("Tip Amount")

fig.suptitle("Restaurant Tipping Dashboard")
plt.tight_layout()
plt.show()