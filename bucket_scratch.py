import s3fs

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

MY_BUCKET = "abovet_sspcloud"
fs.ls(MY_BUCKET)

print(fs.ls(''))