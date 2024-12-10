import s3fs

import pandas as pd
import geopandas as gpd

#read file
glace_arctique = pd.read_csv("glace_arctique.csv")

print(glace_arctique.head())

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

MY_BUCKET = "abovet"
print(fs.ls(MY_BUCKET))

FILE_PATH_OUT_S3 = f"{MY_BUCKET}/diffusion/glace_arctique.csv"

#écrire le fichier dans diffusion
with fs.open(FILE_PATH_OUT_S3, "w") as file_out:
    glace_arctique.to_csv(file_out)

#lire le fichier en local
with fs.open(FILE_PATH_OUT_S3, "r") as file_in:
    df_dpe = pd.read_csv(file_in)

# Vérification
print(df_dpe.head(2))

#importer des dossier

fs.put("zones_ornithologiques/", f"{MY_BUCKET}/diffusion/zones_ornithologiques/", recursive=True)

# Récupération des fichiers depuis MinIO vers la machine locale
fs.get(f"{MY_BUCKET}/diffusion/zones_ornithologiques/", "zones_ornithologiques2/", recursive=True)

df_zones = gpd.read_file("zones_ornithologiques2/")
print(df_zones.head(2))


BUCKET_EVE = "esam"
FILE_PATH_OUT_S3_EVE = f"{BUCKET_EVE}/diffusion/eBird/ebd_atlpuf_relSep-2024.txt"
#lire le fichier en local
with fs.open(FILE_PATH_OUT_S3_EVE, "r") as file_in:
    df_eBird = pd.read_csv(file_in, sep="\t")

print(df_eBird.head(2))



"commande pour résoudre le pbm dans terminal pip install pyopenssl --upgrade"