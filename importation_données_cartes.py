import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, LineString, Point
import matplotlib
import contextily as ctx

# Utiliser un backend compatible
matplotlib.use('Agg')

# Chemin vers le fichier .shp
fichier_shp = "/Users/audrey/projet_python_2024_ENSAE/zones_ornithologiques"

# Lecture du fichier shapefile
gdf = gpd.read_file(fichier_shp)

# Affichage des premières lignes du GeoDataFrame
print(gdf.head())

# Transformation en EPSG:4326 si nécessaire
if gdf.crs != "EPSG:4326":
    gdf = gdf.to_crs(epsg=4326)
print("Système de projection (CRS) :", gdf.crs)

# Conversion des géométries 3D en 2D
def convert_to_2d(geom):
    if geom is None:
        return None
    if geom.has_z:
        if isinstance(geom, Polygon):
            return Polygon([[x, y] for x, y, z in geom.exterior.coords])
        elif isinstance(geom, LineString):
            return LineString([[x, y] for x, y, z in geom.coords])
        elif isinstance(geom, Point):
            return Point(geom.x, geom.y)
    return geom

gdf["geometry"] = gdf["geometry"].apply(convert_to_2d)
print("Conversion en 2D terminée.")

# Vérification des géométries invalides
gdf = gdf[gdf.is_valid]
print("Nombre de géométries valides :", len(gdf))

'''
# Affichage de la carte et sauvegarde dans un fichier
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
gdf.plot(ax=ax, edgecolor='black', cmap='Set2')
ax.set_title("Carte du Shapefile")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.grid()

# Sauvegarder la carte dans un fichier PNG
plt.savefig("/home/onyxia/work/projet_python_2024_ENSAE/carte_shapefile2.png")
print("Carte sauvegardée sous 'carte_shapefile2.png'")
'''

# Affichage de la carte et ajout du fond de carte
fig, ax = plt.subplots(1, 1, figsize=(12, 10))

# Plotting du GeoDataFrame
gdf.plot(ax=ax, edgecolor='black', cmap='Set2')

# Ajout d'un fond de carte via contextily (ici OpenStreetMap)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)

# Personnalisation du graphique
ax.set_title("Carte du Shapefile avec fond OpenStreetMap")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.grid()

# Sauvegarder la carte dans un fichier PNG
plt.savefig("/Users/audrey/projet_python_2024_ENSAE/carte_shapefile2.png")
plt.show()
print("Carte sauvegardée sous 'carte_shapefile2.png'")


