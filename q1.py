#ARYAN SHARMA 16015025070
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')

df = pd.read_csv("dataset.csv")

df.columns = df.columns.str.strip().str.lower()

print(df.head())


plt.figure(figsize=(9, 6))
sns.boxplot(data=df, x='machine', y='diameter', hue='shift')
plt.title('Diameter by Machine and Shift')
plt.xlabel('Machine')
plt.ylabel('Diameter (mm)')
plt.legend(title='Shift')
plt.tight_layout()
plt.savefig("q1_boxplot.png")
plt.show()


df1 = df[df['shift'].isin(['Morning', 'Afternoon'])]

plt.figure(figsize=(9, 6))
sns.violinplot(
    data=df1, x='machine', y='diameter',
    hue='shift', split=True
)
plt.title('Diameter Distribution by Machine')
plt.xlabel('Machine')
plt.ylabel('Diameter (mm)')
plt.legend(title='Shift')
plt.tight_layout()
plt.savefig("q1_violinplot.png")
plt.show()


plt.figure(figsize=(9, 6))
sns.swarmplot(
    data=df, x='machine', y='diameter',
    hue='shift', size=6
)
plt.title('Individual Diameter Measurements')
plt.xlabel('Machine')
plt.ylabel('Diameter (mm)')
plt.legend(title='Shift')
plt.tight_layout()
plt.savefig("q1_swarmplot.png")
plt.show()


result = df.groupby('machine')['diameter'].std()

print("\nStandard deviation of each machine:")
print(result)

print("\nMachine with the highest variation:", result.idxmax())