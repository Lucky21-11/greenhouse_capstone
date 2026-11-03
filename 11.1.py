import pandas as pd
from scipy.stats import chi2_contingency, pearsonr, spearmanr

df = pd.read_csv("titanic.csv")

table1 = pd.crosstab(df['sex'], df['survived'])
print("Sex vs Survived:")
print(table1)

chi2, p, dof, expected = chi2_contingency(table1)

print("\nChi-Square Test (Sex vs Survived)")
print("Chi-Square:", chi2)
print("P-value:", p)

if p < 0.05:
    print("There is a significant association between gender and survival.")
else:
    print("There is no significant association between gender and survival.")

table2 = pd.crosstab(df['pclass'], df['survived'])
print("\nPassenger Class vs Survived:")
print(table2)

chi2, p, dof, expected = chi2_contingency(table2)

print("\nChi-Square Test (Pclass vs Survived)")
print("Chi-Square:", chi2)
print("P-value:", p)

if p < 0.05:
    print("There is a significant association between passenger class and survival.")
else:
    print("There is no significant association between passenger class and survival.")

data = df[['age', 'fare']].dropna()

pearson, p1 = pearsonr(data['age'], data['fare'])
spearman, p2 = spearmanr(data['age'], data['fare'])

print("\nCorrelation between Age and Fare")
print("Pearson Correlation:", pearson)
print("Pearson P-value:", p1)
print("Spearman Correlation:", spearman)
print("Spearman P-value:", p2)

if abs(pearson) < 0.3:
    print("Pearson indicates a weak linear correlation.")
elif abs(pearson) < 0.7:
    print("Pearson indicates a moderate linear correlation.")
else:
    print("Pearson indicates a strong linear correlation.")

if p1 < 0.05:
    print("Pearson correlation is statistically significant.")
else:
    print("Pearson correlation is not statistically significant.")

if p2 < 0.05:
    print("Spearman correlation is statistically significant.")
else:
    print("Spearman correlation is not statistically significant.")