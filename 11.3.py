import seaborn as sns
from scipy import stats
import pandas as pd

df = pd.read_csv("penguins.csv")

print("Shapiro-Wilk Normality Test")
for species in df['species'].unique():
    data = df[df['species'] == species]['flipper_length_mm'].dropna()
    w, p = stats.shapiro(data)
    print(species, "W:", w, "p-value:", p)
    print("Normal" if p > 0.05 else "Not Normal")

adelie = df[df['species'] == 'Adelie']['flipper_length_mm'].dropna()
chinstrap = df[df['species'] == 'Chinstrap']['flipper_length_mm'].dropna()

u, p = stats.mannwhitneyu(adelie, chinstrap)
print("\nMann-Whitney U Test")
print("U-statistic:", u)
print("p-value:", p)

groups = [
    df[df['species'] == species]['bill_length_mm'].dropna()
    for species in df['species'].unique()
]

h, p = stats.kruskal(*groups)
print("\nKruskal-Wallis Test")
print("H-statistic:", h)
print("p-value:", p)

torgersen = df[df['island'] == 'Torgersen']['body_mass_g'].dropna()
dream = df[df['island'] == 'Dream']['body_mass_g'].dropna()

ks, p = stats.ks_2samp(torgersen, dream)
print("\nKolmogorov-Smirnov Test")
print("KS-statistic:", ks)
print("p-value:", p)