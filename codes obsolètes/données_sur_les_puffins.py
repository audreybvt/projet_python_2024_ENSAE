import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import os

# Chemin du fichier d'entrée et sortie
input_path = "/home/onyxia/projet_python_2024_ENSAE/biogeographic_regions.kml"
output_dir = "/home/onyxia/work/projet_python_2024_ENSAE/"
os.makedirs(output_dir, exist_ok=True)  # Créer le répertoire si nécessaire
output_path = os.path.join(output_dir, "carte_waterbird.png")

# Lire le fichier KML
gdf = gpd.read_file(input_path, driver="KML")

# Convertir les coordonnées au système EPSG:3857 (nécessaire pour les basemaps)
gdf = gdf.to_crs(epsg=3857)

# Créer la figure et les axes
fig, ax = plt.subplots(figsize=(12, 12))

# Afficher les données géographiques
gdf.plot(ax=ax, alpha=0.7, edgecolor="black", cmap="tab10")

# Ajouter un fond de carte OpenStreetMap
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# Ajouter un titre
ax.set_title("Carte avec fond OpenStreetMap", fontsize=16)

# Enregistrer la carte dans un fichier PNG
plt.savefig(output_path, dpi=300)
print(f"Carte enregistrée avec succès sous : {output_path}")
