import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Paramètres
theta = np.linspace(0, 2 * np.pi, 200)   # Angle principal
w = np.linspace(-0.3, 0.3, 50)           # Largeur du ruban
theta, w = np.meshgrid(theta, w)

# Équations paramétriques du ruban de Möbius
# (demi-tour sur lui-même)
x = (1 + w * np.cos(theta / 2)) * np.cos(theta)
y = (1 + w * np.cos(theta / 2)) * np.sin(theta)
z = w * np.sin(theta / 2)

# Tracé 3D
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='teal', alpha=0.8, rstride=1, cstride=1, edgecolor='none')

# Titres et axes
ax.set_title("Ruban de Möbius", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
