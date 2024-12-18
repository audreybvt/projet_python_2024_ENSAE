import xarray as xr

# Chemin vers le fichier NetCDF
file_path = "/home/onyxia/projet_python_2024_ENSAE/data/data_SST.nc"

# Charger le fichier NetCDF
data = xr.open_dataset(file_path)

# Explorer les données
print(data)  # Résumé des dimensions, variables et attributs
print(data.variables)  # Liste des variables disponibles


# Accéder à une variable spécifique
print(data['tos'])  # Remplacer par une variable réelle

# Extraire les données d'une variable en tant que tableau NumPy
variable_data = data['tos'].values

# Fermer le fichier pour libérer les ressources
data.close()

import matplotlib
import matplotlib.pyplot as plt
import xarray as xr

# Assuming 'ds' is your xarray Dataset and 'tos' is the variable
# Extract the 'tos' data variable
tos = data['tos']

# Select data for a specific grid point, e.g., i=0 and j=0
tos_at_point = tos.sel(i=0, j=0, method='nearest')


# Plotting sea surface temperature through time
plt.figure(figsize=(10, 6))
tos_at_point.plot()
plt.title('Sea Surface Temperature Over Time (Grid Point: i=0, j=0)')
plt.xlabel('Time')
plt.ylabel('Sea Surface Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
# Enregistrer le graphique dans un fichier (par exemple en PNG)
plt.savefig('/home/onyxia/projet_python_2024_ENSAE/output/sst_time_series.png', dpi=300)

plt.show()





