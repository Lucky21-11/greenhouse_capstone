import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 - Y**2

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, cmap="viridis")
plt.colorbar(label="Z = X² - Y²")
plt.title("Contour Plot of Saddle Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

U = 2 * X
V = -2 * Y

plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V)
plt.title("Gradient Vector Field")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()