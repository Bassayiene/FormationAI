import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Paramètres du système de Lorenz
sigma = 10
rho = 28
beta = 8/3

# Conditions initiales
dt = 0.01
N = 10000
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
x[0], y[0], z[0] = 0., 1., 1.05

# Intégration du système de Lorenz
for i in range(N - 1):
    x[i + 1] = x[i] + sigma * (y[i] - x[i]) * dt
    y[i + 1] = y[i] + (x[i] * (rho - z[i]) - y[i]) * dt
    z[i + 1] = z[i] + (x[i] * y[i] - beta * z[i]) * dt

# Tracé 3D
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='orange', linewidth=0.6)

# Titres et labels
ax.set_title("Attracteur de Lorenz", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
