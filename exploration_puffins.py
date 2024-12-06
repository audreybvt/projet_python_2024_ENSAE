import pandas as pd
import s3fs
import pyarrow as pa

# Tentative de passer par le MinIO Client mais échec total jsp pourquoi
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})
MY_BUCKET = "esam"
eBird_path = f"s3://{MY_BUCKET}/diffusion/eBird/ebd_atlpuf_relSep-2024.txt"
fs.download("diffusion/eBird/ebd_atlpuf_relSep-2024.txt", "test.txt")




# J'ai pété mon crâne et je passe en local 
df = pd.read_csv("/home/onyxia/projet_python_2024_ENSAE/ebd_atlpuf_relSep-2024/ebd_atlpuf_relSep-2024.txt", sep="\t", low_memory=False)
print(df.head())
df.columns








