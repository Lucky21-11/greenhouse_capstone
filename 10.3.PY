#ARYAN SHARMA 16015025070
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

sns.pairplot(df, vars=numeric_cols, hue="species")
plt.show()

corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heat Map of Iris Measurements")
plt.tight_layout()
plt.show()

corr_pairs = corr_matrix.abs().where(
    ~pd.DataFrame(
        [[i == j for j in range(len(numeric_cols))]
         for i in range(len(numeric_cols))],
        index=numeric_cols,
        columns=numeric_cols
    )
).stack()

strongest_pair = corr_pairs.idxmax()
correlation_value = corr_matrix.loc[strongest_pair[0], strongest_pair[1]]

print("Strongest Correlation Pair:", strongest_pair)
print("Correlation Value:", round(correlation_value, 3))