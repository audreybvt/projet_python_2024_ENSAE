
import pandas as pd

# Charger le fichier CSV
file_path ="/Users/audrey/projet_python_2024_ENSAE/F_arctica_attributs.csv"  # Remplace par le chemin de ton fichier CSV
df = pd.read_csv(file_path)

# Afficher le contenu sous forme de tableau
print(df['yrcompiled'].head(10))

import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib

# Charger le fichier shapefile
fichier_shp = "/Users/audrey/projet_python_2024_ENSAE/F_arctica"
gdf = gpd.read_file(fichier_shp)

# Vérifier si les géométries sont valides (facultatif)
gdf = gdf[gdf.is_valid]

# Créer une liste de couleurs différentes pour chaque polygone (ligne)
# Utilisation d'un colormap pour générer des couleurs
cmap = plt.cm.get_cmap("tab20", len(gdf))  # Choisir une palette avec autant de couleurs que de polygones
gdf['color'] = [cmap(i) for i in range(len(gdf))]

# Affichage de la carte avec des couleurs différentes pour chaque polygone
fig, ax = plt.subplots(1, 1, figsize=(12, 10))

# On utilise 'color' pour assigner des couleurs aux polygones et on enlève les contours avec edgecolor='none'
gdf.plot(ax=ax, color=gdf['color'], edgecolor='none')

# Personnalisation du graphique
ax.set_title("Polygones du Shapefile avec couleurs différentes (par ligne, sans contours)")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.grid()

# Sauvegarder la carte dans un fichier PNG
plt.savefig("/Users/audrey/projet_python_2024_ENSAE/F_arctica_polygones_par_ligne.png")
print("Carte sauvegardée sous 'F_arctica_polygones_par_ligne.png'")
