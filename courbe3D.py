import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Paramètre t
t = np.linspace(0, 30, 500)

# Courbe : hélice
x = np.cos(t)
y = np.sin(t)
z = t

# Création du graphique
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracé
ax.plot3D(x, y, z, 'b', linewidth=2)

# Titres et labels
ax.set_title("Courbe 3D : Hélice")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
