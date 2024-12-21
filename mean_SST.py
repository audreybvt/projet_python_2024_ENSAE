import xarray as xr
import matplotlib.pyplot as plt

# Chemin vers le fichier NetCDF
file_path = "/home/onyxia/projet_python_2024_ENSAE/data/data_SST.nc"

# Charger le fichier NetCDF
data = xr.open_dataset(file_path)

# Vérification de la structure des données
print(data)

# Supposons que la variable de température s'appelle 'tos'
tos = data['tos']

# Conversion en moyennes annuelles
tos_annual_mean = tos.resample(time="1Y").mean()

# Affichage de la série temporelle de la moyenne annuelle
plt.figure(figsize=(10, 6))
tos_annual_mean.sel(i=0, j=0, method='nearest').plot()
plt.title('Annual Mean Sea Surface Temperature Over Time (Grid Point: i=0, j=0)')
plt.xlabel('Time')
plt.ylabel('Annual Mean Sea Surface Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()

# Enregistrer le graphique
plt.savefig('/home/onyxia/projet_python_2024_ENSAE/output/annual_sst_time_series.png', dpi=300)

plt.show()

# Sauvegarde des données moyennées annuellement dans un nouveau fichier NetCDF
output_path = "/home/onyxia/projet_python_2024_ENSAE/output/annual_mean_SST.nc"
tos_annual_mean.to_netcdf(output_path)

print(f"Fichier NetCDF avec moyennes annuelles enregistré : {output_path}")

# Fermer les ressources
data.close()


# Chemin vers le fichier NetCDF
file_path = "/home/onyxia/projet_python_2024_ENSAE/data/tos_Omon_HadGEM3-GC31-LL_ssp245_r1i1p1f3_gn_20150116-20491216.nc"

# Charger le fichier NetCDF
data = xr.open_dataset(file_path)

# Vérification de la structure des données
print(data)

# Supposons que la variable de température s'appelle 'tos'
tos = data['tos']

# Conversion en moyennes annuelles
tos_annual_mean = tos.resample(time="1Y").mean()

# Affichage de la série temporelle de la moyenne annuelle
plt.figure(figsize=(10, 6))
tos_annual_mean.sel(i=0, j=0, method='nearest').plot()
plt.title('Annual Mean Sea Surface Temperature Over Time (Grid Point: i=0, j=0)')
plt.xlabel('Time')
plt.ylabel('Annual Mean Sea Surface Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()

# Enregistrer le graphique
plt.savefig('/home/onyxia/projet_python_2024_ENSAE/output/annual_sst_time_series_scenariossp245.png', dpi=300)

plt.show()

# Sauvegarde des données moyennées annuellement dans un nouveau fichier NetCDF
output_path = "/home/onyxia/projet_python_2024_ENSAE/output/annual_mean_SST_scenariossp245.nc"
tos_annual_mean.to_netcdf(output_path)

print(f"Fichier NetCDF avec moyennes annuelles enregistré : {output_path}")

# Fermer les ressources
data.close()
