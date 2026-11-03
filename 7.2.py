#ARYAN SHARMA 16015025070
import numpy as np

temp = np.random.randint(15, 46, 30)
print("Temperatures:", temp)

extreme = np.sum(temp > 40)
print("Extreme heat days:", extreme)

temp = np.where(temp < 20, -1, temp)
print("After replacement:", temp)

mean = np.mean(temp)
std = np.std(temp)

result = temp[(temp >= mean - std) & (temp <= mean + std)]
print("Within 1 standard deviation:", result)