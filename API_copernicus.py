import cdsapi
import pandas as pd
import s3fs
import zipfile
import xarray as xr



#Code Eve API Climate Data Store Copernicus
with open('/home/onyxia/.cdsapirc', 'w') as file:
    file.write("""
    url: https://cds.climate.copernicus.eu/api
    key: 4a3c4e19-b15f-41a9-8374-adf4f8ee3fb3
    """)

#API CDS Copernicus
# Model ... - from 2000 to 2014 - SST - historical data 

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

#Dezippage du fichier téléchargé localement
local_zip_path = "/home/onyxia/work/cds_output.zip"
temp_dir = "./extracted_files" # Dossier temporaire pour extraire les fichiers
with zipfile.ZipFile(local_zip_path, 'r') as zip_ref: # Ouvrez le fichier ZIP et extrayez son contenu
    zip_ref.extractall(temp_dir)
print(f"Fichiers extraits dans : {temp_dir}")

# Charger la liste des fichiers extraits dans un DataFrame
extracted_files_cds = pd.DataFrame({"file_paths": zip_ref.namelist()})
print("Fichiers extraits :")
print(extracted_files_cds)


#Vérif du fichier
file_path = "/home/onyxia/work/extracted_files/tos_Omon_MPI-ESM1-2-HR_historical_r1i1p1f1_gn_20000116-20140616.nc"
dataset = xr.open_dataset(file_path)
print(dataset)




#Ecriture des données issues de l'API CDS sur MinIO Client

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




# Exploration des données
fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})
MY_BUCKET = "esam"
minio_path = f"{MY_BUCKET}/diffusion/cds_data/tos_Omon_MPI-ESM1-2-HR_historical_r1i1p1f1_gn_20000116-20140616.nc"

local_file = "temp_file.nc"
with fs.open(minio_path, "rb") as minio_file:
    with open(local_file, "wb") as local_nc_file:
        local_nc_file.write(minio_file.read())

# Charger le fichier localement avec xarray
dataset = xr.open_dataset(local_file, engine="netcdf4")
print(dataset)

df_cds = dataset.to_dataframe().reset_index()
print(df_cds.head())

df_cds_clean = df_cds.dropna(subset=["tos"])
print(df_cds_clean.head())


df_cds_clean.to_csv("projet_python_2024_ENSAE/sst_data_cds.csv", index=False)




#### Climate Data Storage Copernicus 2 ####
# Model HadGEM3-GC31-LL (UK) - from 2015 to 2049 - SST - SSP5-8.5 (worst scenario)


client = cdsapi.Client()
dataset = "projections-cmip6"
request = {
    "temporal_resolution": "monthly",
    "variable": "sea_surface_temperature",
    "experiment": "ssp5_8_5",
    "model": "hadgem3_gc31_ll",
    "month": ["01", "06"],
    "year": [
        "2015", "2016", "2017",
        "2018", "2019", "2020",
        "2021", "2022", "2023",
        "2024", "2025", "2026",
        "2027", "2028", "2029",
        "2030", "2031", "2032",
        "2033", "2034", "2035",
        "2036", "2037", "2038",
        "2039", "2040", "2041",
        "2042", "2043", "2044",
        "2045", "2046", "2047",
        "2048", "2049"
    ],
    "area": [68.5, -27, 61.5, -10],  # Zone : Nord, Ouest, Sud, Est
}
client.retrieve(dataset, request).download()

local_zip_path_2 = "/home/onyxia/work/cds_output_2.zip"
temp_dir = "./extracted_files" # Dossier temporaire pour extraire les fichiers
with zipfile.ZipFile(local_zip_path, 'r') as zip_ref: # Ouvrez le fichier ZIP et extrayez son contenu
    zip_ref.extractall(temp_dir)
print(f"Fichiers extraits dans : {temp_dir}")

# Charger la liste des fichiers extraits dans un DataFrame
extracted_files_cds = pd.DataFrame({"file_paths": zip_ref.namelist()})
print("Fichiers extraits :")
print(extracted_files_cds)