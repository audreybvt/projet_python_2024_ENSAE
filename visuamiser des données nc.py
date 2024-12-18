import xarray as xr

# Chemin vers le fichier NetCDF
file_path = "/home/onyxia/projet_python_2024_ENSAE/data/data_SST.nc"

# Charger le fichier NetCDF
data = xr.open_dataset(file_path)

# Explorer les données
print(data)  # Résumé des dimensions, variables et attributs
print(data.variables)  # Liste des variables disponibles


# Accéder à une variable spécifique
print(data['sea_surface_temperature'])  # Remplacer par une variable réelle

# Extraire les données d'une variable en tant que tableau NumPy
variable_data = data['sea_surface_temperature'].values

# Fermer le fichier pour libérer les ressources
data.close()

import matplotlib.pyplot as plt

# Exemple : Lire et visualiser la température de surface
temperature = data['sea_surface_temperature']  # Remplacer 'tos' par le nom réel de la variable

# Sélectionner une tranche temporelle spécifique (si pertinent)
temperature_at_time = temperature.isel(time=0)  # Première étape temporelle

# Tracer la variable
temperature_at_time.plot()
plt.title("Température de surface des océans (temps=0)")
plt.show()
