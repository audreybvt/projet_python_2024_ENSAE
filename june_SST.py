import xarray as xr
import matplotlib.pyplot as plt

# Chemin vers le fichier NetCDF
file_path = "data/data_SST.nc"

# Charger le fichier NetCDF
data = xr.open_dataset(file_path)

# Vérification de la structure des données
print(data)

# Supposons que la variable de température s'appelle 'tos'
tos = data['tos']

# Filtrer uniquement les données de juin
tos_june = tos.sel(time=tos['time'].dt.month == 6)

# Calculer les moyennes pour le mois de juin (par année)
tos_june_mean = tos_june.resample(time="1Y").mean()

# Affichage de la série temporelle de la moyenne de juin
plt.figure(figsize=(10, 6))
tos_june_mean.sel(i=0, j=0, method='nearest').plot()
plt.title('June Mean Sea Surface Temperature Over Time (Grid Point: i=0, j=0)')
plt.xlabel('Time')
plt.ylabel('June Mean Sea Surface Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()

# Enregistrer le graphique
plt.savefig('output/june_sst_time_series.png', dpi=300)

plt.show()

# Sauvegarde des données moyennes de juin dans un nouveau fichier NetCDF
output_path = "output/june_mean_SST.nc"
tos_june_mean.to_netcdf(output_path)

print(f"Fichier NetCDF avec moyennes de juin enregistré : {output_path}")

# Fermer les ressources
data.close()


# Répéter le processus pour le fichier du scénario SSP585
file_path = "data/tos_Omon_HadGEM3-GC31-LL_ssp585_r1i1p1f3_gn_20150116-20491216.nc"

# Charger le fichier NetCDF
data = xr.open_dataset(file_path)

# Vérification de la structure des données
print(data)

# Supposons que la variable de température s'appelle 'tos'
tos = data['tos']

# Filtrer uniquement les données de juin
tos_june = tos.sel(time=tos['time'].dt.month == 6)

# Calculer les moyennes pour le mois de juin (par année)
tos_june_mean = tos_june.resample(time="1Y").mean()

# Affichage de la série temporelle de la moyenne de juin
plt.figure(figsize=(10, 6))
tos_june_mean.sel(i=0, j=0, method='nearest').plot()
plt.title('June Mean Sea Surface Temperature Over Time (Grid Point: i=0, j=0, SSP585)')
plt.xlabel('Time')
plt.ylabel('June Mean Sea Surface Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()

# Enregistrer le graphique
plt.savefig('output/june_sst_time_series_scenariossp585.png', dpi=300)

plt.show()

# Sauvegarde des données moyennes de juin dans un nouveau fichier NetCDF
output_path = "output/june_mean_SST_scenariossp585.nc"
tos_june_mean.to_netcdf(output_path)

print(f"Fichier NetCDF avec moyennes de juin enregistré : {output_path}")

# Fermer les ressources
data.close()
