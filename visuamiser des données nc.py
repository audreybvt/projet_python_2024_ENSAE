import xarray as xr

# Chemin vers le fichier NetCDF
file_path = "/home/onyxia/projet_python_2024_ENSAE/data/data_SST.nc"

# Charger le fichier NetCDF
data = xr.open_dataset(file_path)

# Explorer les données
print(data)  # Résumé des dimensions, variables et attributs
print(data.variables)  # Liste des variables disponibles

'''
# Accéder à une variable spécifique
print(data['nom_de_la_variable'])  # Remplacer par une variable réelle

# Extraire les données d'une variable en tant que tableau NumPy
variable_data = data['nom_de_la_variable'].values

# Fermer le fichier pour libérer les ressources
data.close()
'''