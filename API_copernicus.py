import cdsapi
import pandas as pd
import s3fs
import zipfile
import xarray as xr

with open('/home/onyxia/.cdsapirc', 'w') as file:
    file.write("""
    url: https://cds.climate.copernicus.eu/api
    key: 4a3c4e19-b15f-41a9-8374-adf4f8ee3fb3
    """)

client = cdsapi.Client()
dataset = "projections-cmip6"
request = {
    "temporal_resolution": "monthly",
    "experiment": "historical",
    "variable": "sea_surface_temperature",
    "model": "mpi_esm1_2_hr",
    "month": ["01", "06"],
    "year": [
        "2000", "2001", "2002",
        "2003", "2004", "2005",
        "2006", "2007", "2008",
        "2009", "2010", "2011",
        "2012", "2013", "2014"
    ],
    "area": [68.5, -27, 61.5, -10],  # Zone : Nord, Ouest, Sud, Est
}
client.retrieve(dataset, request).download()


# Chemin local du fichier ZIP téléchargé
local_zip_path = "/home/onyxia/work/cds_output.zip"

# Dossier temporaire pour extraire les fichiers
temp_dir = "./extracted_files"

# Ouvrez le fichier ZIP et extrayez son contenu
with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)

print(f"Fichiers extraits dans : {temp_dir}")

# Charger la liste des fichiers extraits dans un DataFrame
extracted_files_cds = pd.DataFrame({"file_paths": zip_ref.namelist()})
print("Fichiers extraits :")
print(extracted_files_cds)





# Chemin du fichier NetCDF
file_path = "/home/onyxia/work/extracted_files/tos_Omon_MPI-ESM1-2-HR_historical_r1i1p1f1_gn_20000116-20140616.nc"

# Charger et afficher les métadonnées
dataset = xr.open_dataset(file_path)
print(dataset)





# Tentative avec l'API mais échec

# Initialiser MiniO
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})
MY_BUCKET = "esam"
print(fs.ls(MY_BUCKET))

minio_path = f'{MY_BUCKET}/diffusion/cds_data/tos_Omon_MPI-ESM1-2-HR_historical_r1i1p1f1_gn_20000116-20140616.nc'


# Télécharger directement les données sur MiniO
dataset = "projections-cmip6"
request = {
    "temporal_resolution": "monthly",
    "experiment": "historical",
    "variable": "sea_surface_temperature",
    "model": "mpi_esm1_2_hr",
    "month": ["01", "06"],
    "year": [
        "2000", "2001", "2002",
        "2003", "2004", "2005",
        "2006", "2007", "2008",
        "2009", "2010", "2011",
        "2012", "2013", "2014"
    ],
    "area": [68.5, -27, 61.5, -10],  # Zone : Nord, Ouest, Sud, Est
}

with fs.open(minio_path, "wb") as minio_file:  # Fichier cible sur MinIO
    with open(file_path, "rb") as local_file:  # Fichier source local
        minio_file.write(local_file.read())

print(fs.ls(f"{MY_BUCKET}/diffusion/cds_data"))
