
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

birth_months = [
    "January", "March", "May", "January",
    "June", "August", "March", "October",
    "December", "May", "July", "January", "June"
]

count = {}

for month in birth_months:
    count[month] = count.get(month, 0) + 1

print("Total students:", len(birth_months))
print("\nStudents in each birth month:")

for month in months:
    if month in count:
        print(month, ":", count[month])

print("\nMonths shared by two or more students:")

for month, total in count.items():
    if total >= 2:
        print(month, ":", total, "students")
