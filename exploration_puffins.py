import pandas as pd
import s3fs
import pyarrow as pa

# Tentative de passer par le MinIO Client mais échec total jsp pourquoi
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})
MY_BUCKET = "esam"
eBird_path = f"s3://{MY_BUCKET}/diffusion/eBird/ebd_atlpuf_relSep-2024.txt"
with fs.open(eBird_path, "r") as file_in:
    eBird_df = pd.read_csv(file_in, sep="\t")
print(eBird_df.head())

fs.download("diffusion/eBird/ebd_atlpuf_relSep-2024.txt", "test.txt")




import copernicusmarine 
from copernicusmarine import get 


data_request = {
   "dataset_id_sst_gap_l3s" : "cmems_obs-sst_atl_phy_nrt_l3s_P1D-m",
   "longitude" : [-6.17, -5.09], 
   "latitude" : [35.75, 36.29],
   "time" : ["2023-01-01", "2023-01-31"],
   "variables" : ["sea_surface_temperature"]
}

copernicusmarine.get(
    dataset_id = 'cmems_obs-sst_atl_phy_nrt_l3s_P1D-m'
)








