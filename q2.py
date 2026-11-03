import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip().str.lower()

print(df.head())


plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="department", hue="study_mode")
plt.title("Students in Each Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("q2_countplot.png")
plt.show()


plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="department", y="marks", hue="study_mode", errorbar=None)
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("q2_barplot.png")
plt.show()


plt.figure(figsize=(8, 6))
sns.pointplot(data=df, x="department", y="marks", hue="study_mode", errorbar=None)
plt.title("Average Marks Across Departments")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("q2_pointplot.png")
plt.show()


plt.figure(figsize=(8, 6))
sns.stripplot(data=df, x="department", y="marks", hue="study_mode", dodge=True, size=6)
plt.title("Individual Student Marks")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("q2_stripplot.png")
plt.show()


avg = df.groupby("department")["marks"].mean()
print("\nAverage marks:")
print(avg)


std = df.groupby("department")["marks"].std()
print("\nVariation in marks:")
print(std)

print("\nDepartment with highest average marks:", avg.idxmax())
print("Department with highest variation:", std.idxmax())