import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# Lire le fichier KML
gdf = gpd.read_file("/home/onyxia/projet_python_2024_ENSAE/biogeographic_regions.kml", driver="KML")

# Convertir les coordonnées au système EPSG:3857 (nécessaire pour les basemaps)
gdf = gdf.to_crs(epsg=3857)

# Afficher la carte
ax = gdf.plot(figsize=(12, 12), alpha=0.7, edgecolor="black", cmap="tab10")

# Ajouter un fond de carte OpenStreetMap
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# Ajouter un titre
plt.title("Carte avec fond OpenStreetMap", fontsize=16)
plt.savefig("/home/onyxia/work/projet_python_2024_ENSAE/carte_waterbird.png")
