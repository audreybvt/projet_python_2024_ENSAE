
import xarray as xr

###################### VISUALISER LES DONNEES COPERNICUS ####################

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



#########################@ VISUALISER LES DIFFERENTS SCENARI #############################


import xarray as xr
import matplotlib.pyplot as plt

# Chemins vers les fichiers NetCDF
file_paths = [
    "data/tos_Omon_HadGEM3-GC31-LL_ssp126_r1i1p1f3_gn_20150116-20491216.nc",  # Scénario 1
    "data/tos_Omon_HadGEM3-GC31-LL_ssp245_r1i1p1f3_gn_20150116-20491216.nc",  # Scénario 2
    "data/tos_Omon_HadGEM3-GC31-LL_ssp585_r1i1p1f3_gn_20150116-20491216.nc"   # Scénario 3
]

# Noms des scénarios pour la légende
scenario_names = ["SSP1-2.6", "SSP2-4.5", "SSP5-8.5"]

# Initialisation du graphique
plt.figure(figsize=(12, 8))

# Parcourir les fichiers et les ajouter au graphique
for i, file_path in enumerate(file_paths):
    # Charger les données du fichier NetCDF
    data = xr.open_dataset(file_path)
    
    # Extraire les données de température de surface de la mer (tos)
    tos = data['tos']
    
    # Sélectionner un point de grille spécifique (par exemple, i=0, j=0)
    tos_at_point = tos.sel(i=0, j=0, method='nearest')
    
    # Ajouter les données au graphique
    plt.plot(
        tos_at_point['time'],  # Axe des x : temps
        tos_at_point,          # Axe des y : température de surface de la mer
        label=scenario_names[i]  # Légende basée sur le scénario
    )
    
    # Fermer le fichier NetCDF pour libérer les ressources
    data.close()

# Personnalisation du graphique
plt.title('Évolution de la Température de Surface de la Mer pour Différents Scénarios')
plt.xlabel('Temps')
plt.ylabel('Température de Surface de la Mer (°C)')
plt.legend(title="Scénarios", loc='upper left')  # Afficher la légende
plt.grid(True)
plt.xticks(rotation=45)  # Rotation des étiquettes de l'axe des x
plt.tight_layout()

# Enregistrer le graphique
plt.savefig('/home/onyxia/projet_python_2024_ENSAE/output/sst_scenarios_comparison.png', dpi=300)

# Afficher le graphique
plt.show()
