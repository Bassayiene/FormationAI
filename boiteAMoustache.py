import matplotlib.pyplot as plt
import numpy as np

# Génération de données aléatoires
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(120, 15, 200)

# Création du boxplot
plt.figure(figsize=(6, 5))
plt.boxplot([data1, data2, data3],
            labels=['Groupe A', 'Groupe B', 'Groupe C'],
            patch_artist=True,
            boxprops=dict(facecolor='lightblue'))

plt.title("Boîte à moustaches (Boxplot)")
plt.ylabel("Valeurs mesurées")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
