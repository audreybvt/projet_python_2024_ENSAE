# Creation of a bucket on MinIO Client 

import s3fs

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

MY_BUCKET = "esam"
fs.ls(MY_BUCKET)

# Creation of the folder diffusion, accessible by everyone 
fs.touch(f"{MY_BUCKET}/diffusion")


# Import of eBird dataset on Atlantic puffin in the folder diffusion
FILE_PATH_OUT_S3 = f"{MY_BUCKET}/diffusion/eBirdSep2024.parquet"
eBird = "/home/onyxia/projet_python_2024_ENSAE/ebd_atlpuf_relSep-2024"
fs.put(eBird, f"{MY_BUCKET}/diffusion/eBird", recursive = True)

# with fs.open(FILE_PATH_OUT_S3, "wb") as file_out: eBirdSep2024.to_parquet(file_out)
ImportantBirdSanctuaries = "/home/onyxia/work/projet_python_2024_ENSAE-1/NI_F25v_ImportantBirdSanctuaries_SHP"
# Import of Bird Sanctuaries in the folder diffusion
fs.put(ImportantBirdSanctuaries, f"{MY_BUCKET}/diffusion/ImportantBirdSanctuaries", recursive=True)

# Use of Eve Samani bucket