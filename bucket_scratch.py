import s3fs
import io
import os
import requests
import zipfile
'''
# Chemin vers le fichier .shp
fichier_shp = "/home/onyxia/work/projet_python_2024_ENSAE/zones_ornithologiques"

# Lecture du fichier shapefile
gdf = gpd.read_file(fichier_shp)

# Affichage des premières lignes du GeoDataFrame
print(gdf.head())

'''
'''

# Spécifiez le dossier contenant les fichiers du shapefile
dossier_shp = "/home/onyxia/work/projet_python_2024_ENSAE/zones_ornithologiques.shp"

# Liste des fichiers associés au shapefile (fichier.shp, fichier.shx, fichier.dbf, etc.)
fichiers_shp = [f for f in os.listdir(dossier_shp) if f.endswith(('.shp', '.shx', '.dbf', '.prj'))]

# Chemin vers le fichier ZIP de sortie
fichier_zip = "/home/onyxia/work/projet_python_2024_ENSAE/zones_ornithologiques.zip"

# Créer le fichier ZIP et y ajouter les fichiers
with zipfile.ZipFile(fichier_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for fichier in fichiers_shp:
        chemin_complet = os.path.join(dossier_shp, fichier)
        zipf.write(chemin_complet, os.path.basename(chemin_complet))  # Ajouter le fichier au ZIP

print(f"Les fichiers ont été compressés dans le fichier ZIP : {fichier_zip}")


fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})


MY_BUCKET = "abovet"
fs.ls(MY_BUCKET)


fs.put("zones_ornithologiques/", f"{MY_BUCKET}/diffusion/zones_ornithologiques/", recursive=True)import s3fs
import geopandas as gpd
'''





import s3fs

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

MY_BUCKET = "esam"
fs.ls(MY_BUCKET)

FILE_PATH_OUT_S3 = f"{MY_BUCKET}/diffusion/zones_ornithologiques"
fs.put("zones_ornithologiques/", f"{MY_BUCKET}/diffusion/zones_ornithologiques/", recursive=True)


