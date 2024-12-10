import s3fs

import pandas as pd

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
# Import
with fs.open(FILE_PATH_OUT_S3, "r") as file_in:
    df_dpe = pd.read_csv(file_in)

# Vérification
print(df_dpe.head(2))

#importer des dossier

fs.put("zones_ornithologiques/", f"{MY_BUCKET}/diffusion/zones_ornithologiques/", recursive=True)

"commande pour résoudre le pbm dans terminal pip install pyopenssl --upgrade"