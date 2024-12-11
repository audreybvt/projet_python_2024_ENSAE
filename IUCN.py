import pandas as pd
import s3fs 
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

MY_BUCKET = "esam"
print(fs.ls(MY_BUCKET))

fs.put("/home/onyxia/work/projet_python_2024_ENSAE/IUCN_redlist", f"{MY_BUCKET}/diffusion/", recursive=True)


# Récupération des fichiers depuis MinIO vers la machine locale
fs.get(f"{MY_BUCKET}/diffusion/IUCN_redlist/", "IUCN_redlist/", recursive=True)



# Charger le fichier shapefile
shp_file_path = "/home/onyxia/work/IUCN_redlist/data_0.shp"
gdf = gpd.read_file(shp_file_path)

# Afficher les premières lignes
print(gdf.head())

# Afficher les colonnes disponibles
print("Colonnes disponibles :", gdf.columns)

# Résumé des données géométriques
print(gdf.geometry.head())

matplotlib.use('TkAgg')  # Utilisez un backend adapté
# Afficher les données sous forme de carte
gdf.plot(figsize=(10, 10), edgecolor='black', color='blue')
plt.title("Carte des données géospatiales")
plt.show()

