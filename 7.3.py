#ARYAN SHARMA 16015025070
import numpy as np

marks = np.random.randint(0, 101, (5, 4))

print("Marks:\n", marks)

total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)

print("Student Total:", total)
print("Student Average:", average)

subject_avg = np.mean(marks, axis=0)
subject_highest = np.max(marks, axis=0)

print("Subject Average:", subject_avg)
print("Subject Highest:", subject_highest)

topper = np.argmax(total)
print("Topper Index:", topper)