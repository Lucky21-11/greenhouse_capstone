import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd

df = pd.read_csv("tips.csv")


t, p = stats.ttest_1samp(df['total_bill'], 20)
print("One-Sample T-Test")
print("t-statistic:", t)
print("p-value:", p)
print("Significant difference:", p < 0.05)

smokers = df[df['smoker'] == 'Yes']['tip']
non_smokers = df[df['smoker'] == 'No']['tip']

lev_stat, lev_p = stats.levene(smokers, non_smokers)
print("\nLevene's Test")
print("p-value:", lev_p)

equal_var = lev_p > 0.05
t, p = stats.ttest_ind(smokers, non_smokers, equal_var=equal_var)

print("\nIndependent T-Test")
print("t-statistic:", t)
print("p-value:", p)
print("Significant difference:", p < 0.05)


groups = [df[df['day'] == day]['total_bill']
          for day in ['Thur', 'Fri', 'Sat', 'Sun']]

f, p = stats.f_oneway(*groups)

print("\nOne-Way ANOVA")
print("F-statistic:", f)
print("p-value:", p)
print("At least one day differs:", p < 0.05)


before = np.array([150, 145, 160, 155, 148, 162, 158, 151, 149, 156])
after  = np.array([140, 138, 150, 148, 142, 153, 149, 145, 140, 147])

t, p = stats.ttest_rel(before, after)

print("\nPaired T-Test")
print("t-statistic:", t)
print("p-value:", p)
print("Significant improvement:", p < 0.05)