import pandas as pd
import s3fs

# Configuration des identifiants AWS
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})
  # anon=False pour utiliser vos identifiants configurés

MY_BUCKET = "esam"
FILE_PATH_S3 = f"s3://{MY_BUCKET}/diffusion/eBirdSep2024.parquet"



# Tester l'accès au bucket
print(fs.ls("s3://esam/diffusion/"))

# Tester si le fichier existe
print(fs.exists(FILE_PATH_S3))
print(fs.exists(FILE_PATH_S3))


fs.get(FILE_PATH_S3, "eBirdSep2024.parquet")  # Télécharge le fichier localement
info = fs.info(FILE_PATH_S3)
print(info)





# Lecture directe avec pandas
eBirdSep2024 = pd.read_parquet(FILE_PATH_S3, filesystem=fs)

# Vérification
print(eBirdSep2024.head(2))
