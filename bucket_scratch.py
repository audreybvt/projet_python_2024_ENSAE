import s3fs

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://datalab.sspcloud.fr/my-files"})

MY_BUCKET = "abovet"
fs.ls(MY_BUCKET)

