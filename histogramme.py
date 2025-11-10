import matplotlib.pyplot as plt
import numpy as np

# Génération de données aléatoires
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)  # moyenne=50, écart-type=10

# Création de l'histogramme
plt.figure(figsize=(7, 5))
plt.hist(data, bins=20, color='skyblue', edgecolor='black', alpha=0.7)

# Titres et légendes
plt.title("Histogramme de la distribution des données", fontsize=14)
plt.xlabel("Valeurs")
plt.ylabel("Fréquence")
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()
