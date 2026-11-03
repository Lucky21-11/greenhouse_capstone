import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

df = pd.read_csv("robot.csv")
df.columns = df.columns.str.strip().str.lower()

print(df.head())


g1 = sns.catplot(
    data=df, x="condition", y="battery",
    hue="environment", col="sensor",
    kind="bar", height=4, aspect=1.1,
    errorbar=None
)

g1.fig.suptitle("Battery Consumption by Condition", y=1.05)
g1.set_axis_labels("Condition", "Battery Consumption")
g1.savefig("q4_catplot_bar.png")
plt.show()


g2 = sns.catplot(
    data=df, x="condition", y="battery",
    hue="environment", col="sensor",
    kind="point", height=4, aspect=1.1,
    errorbar=None
)

g2.fig.suptitle("Battery Consumption Trend", y=1.05)
g2.set_axis_labels("Condition", "Battery Consumption")
g2.savefig("q4_catplot_point.png")
plt.show()


g3 = sns.FacetGrid(
    df, row="environment", col="sensor",
    hue="condition", height=3.2, aspect=1.2
)

g3.map(sns.scatterplot, "speed", "battery", s=90)
g3.add_legend()
g3.fig.suptitle("Speed vs Battery Consumption", y=1.03)
g3.set_axis_labels("Speed", "Battery Consumption")
g3.savefig("q4_facetgrid.png")
plt.show()


result = df.groupby(["environment", "condition"])["battery"].mean()

print("\nAverage battery consumption:")
print(result)