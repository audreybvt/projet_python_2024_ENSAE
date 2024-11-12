import geopandas as gpd
import matplotlib.pyplot as plt

# Chemin vers le fichier .shp
fichier_shp = "/home/onyxia/work/projet_python_2024_ENSAE/NI_F25v_mikilvaegFuglasvaedi_SHP"

# Lecture du fichier shapefile
gdf = gpd.read_file(fichier_shp)

# Affichage des premières lignes du GeoDataFrame
print(gdf.head())

# Afficher le système de projection (CRS)
print(gdf.crs)

# Afficher la colonne géométrie
print(gdf.geometry)

# Affichage de la carte
gdf.plot(edgecolor='black', cmap='Set2', figsize=(10, 10))
plt.title("Carte du Shapefile")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid()
plt.show()