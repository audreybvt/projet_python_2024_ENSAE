import xarray as xr
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Charger les données NetCDF (températures)
nc_file = "output/annual_mean_SST.nc"
data = xr.open_dataset(nc_file)

# Moyenne annuelle des températures
temperature = data['tos'].resample(time="1Y").mean().to_dataframe()
temperature.reset_index(inplace=True)

# Vérifier les valeurs dans la colonne 'time' avant conversion
print("Valeurs avant conversion de 'time' dans temperature : ", temperature['time'].head())

# Convertir le 'time' cftime en chaîne de caractères
temperature['time'] = temperature['time'].astype(str)

# Convertir en datetime après la conversion en chaîne
temperature['time'] = pd.to_datetime(temperature['time'])

# Extraire l'année et la convertir en int64
temperature['time'] = temperature['time'].dt.year.astype('int64')


# Vérifier les valeurs après conversion
print("Valeurs après conversion de 'time' dans temperature : ", temperature['time'].head())

# Charger les données CSV (taux de production de puffins)
puffins = pd.read_csv("data/puffin-data1_Data.csv")

# Renommer la colonne 'Year' en 'time' pour correspondre à la colonne de température
puffins.rename(columns={"Year": "time", "Prod": "production_rate"}, inplace=True)

# Vérifier les types de données
print("Types de données de temperature:\n", temperature.dtypes)
print("Types de données de puffins:\n", puffins.dtypes)

# Vérifier si les années de 'temperature' et 'puffins' se correspondent
print("Années disponibles dans temperature:", temperature['time'].unique())
print("Années disponibles dans puffins:", puffins['time'].unique())

# Joindre les données par année (colonne 'time')
merged_data = pd.merge(temperature, puffins[['time', 'production_rate']], on="time", how='inner')

# Vérifier le résultat de la fusion
print("Données après fusion :\n", merged_data.head())

# Vérifier s'il y a des lignes manquantes
print(f"Nombre de lignes manquantes après fusion : {merged_data.isnull().sum().sum()}")


    # Visualiser les données
plt.scatter(merged_data['tos'], merged_data['production_rate'])
plt.title("Température vs Taux de Production des Puffins")
plt.xlabel("Température (°C)")
plt.ylabel("Taux de Production")
plt.show()

    # Préparer les données pour le modèle
X = merged_data[['tos']]  # Température
y = merged_data['production_rate']  # Taux de production

    # Vérifier les valeurs manquantes dans y
print("Valeurs manquantes dans y :", y.isnull().sum())

# Supprimer les lignes où y est manquant, en supprimant aussi les lignes correspondantes dans X
merged_data_clean = merged_data.dropna(subset=['production_rate', 'tos'])

# Vérifier qu'il n'y a plus de NaN dans y après le nettoyage
X_clean = merged_data_clean[['tos']]
y_clean = merged_data_clean['production_rate']

print("Valeurs manquantes après nettoyage dans y_clean :", y_clean.isnull().sum())

# Division en jeu d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_clean, y_clean, test_size=0.2, random_state=42)

# Vérification qu'il n'y a plus de NaN après la division
print("Valeurs manquantes après division dans y_train :", y_train.isnull().sum())
print("Valeurs manquantes après division dans y_test :", y_test.isnull().sum())

# Entraîner un modèle Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Prédictions sur le jeu de test
y_pred = rf_model.predict(X_test)

# Évaluer la performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

'''
# Visualiser les performances
plt.scatter(y_test, y_pred)
plt.title("Prédictions vs Observations (Random Forest)")
plt.xlabel("Observations")
plt.ylabel("Prédictions")
'''
# Créer des couleurs basées sur 'y_test' ou une autre variable, ici on utilise 'y_test' pour la couleur
colors = np.log1p(y_test)  # Exemple de mise à l'échelle des couleurs avec log(y_test + 1))

# Visualisation des prédictions
scatter = plt.scatter(y_test, y_pred, c=colors, cmap='viridis', label='Taux de production', alpha=0.7)

# Ajouter un titre et des étiquettes
plt.title("Prédictions vs Observations (Random Forest)")
plt.xlabel("Observations")
plt.ylabel("Prédictions")

# Ajouter la barre de couleur pour la légende
cbar = plt.colorbar(scatter)  # Associe la barre de couleur à l'objet 'scatter'
cbar.set_label('Valeur (log(y_test + 1))')

plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/prediction_observation_rf.png', dpi=300)
plt.show()


# Scénarios de température
future_scenarios = pd.DataFrame({
    'tos': [X['tos'].mean() + 1, X['tos'].mean() + 2, X['tos'].mean() + 3]
})

# Prédictions pour les scénarios
future_predictions = rf_model.predict(future_scenarios)

# Affichage des prédictions
for i, scenario in enumerate(future_scenarios['tos']):
    print(f"Scénario {i+1} (Température = {scenario:.2f}°C) : Taux de production prévu = {future_predictions[i]:.2f}")

# Visualisation des prédictions pour les scénarios
plt.figure(figsize=(10, 6))
plt.bar(['+1°C', '+2°C', '+3°C'], future_predictions, color='skyblue')
plt.title("Prédictions du Taux de Production des Puffins selon les Scénarios de Température")
plt.ylabel("Taux de Production")
plt.xlabel("Scénarios de Température")
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/predictions.png', dpi=300)
plt.show()

#################### Prévisions avec les prédictions de copernicus #################

# Charger les données futures de température (ici, je suppose un fichier CSV ou NetCDF avec des prévisions)
# Si vous avez un fichier NetCDF avec des températures futures, vous pouvez les charger de la même manière que les données passées.
future_nc_file = "output/annual_mean_SST_scenariossp585.nc"
future_data = xr.open_dataset(future_nc_file)

# Moyenne annuelle des températures futures (pour 2049, par exemple)
future_temperature = future_data['tos'].resample(time="1Y").mean().to_dataframe()
future_temperature.reset_index(inplace=True)

# Convertir le 'time' cftime en chaîne de caractères
future_temperature['time'] = future_temperature['time'].astype(str)

# Convertir en datetime après la conversion en chaîne
future_temperature['time'] = pd.to_datetime(future_temperature['time'])

# Extraire l'année et la convertir en int64
future_temperature['time'] = future_temperature['time'].dt.year.astype('int64')

# Afficher les données futures pour vérifier
print("Données futures de température :\n", future_temperature.head())

# Préparer les données futures (en utilisant la température moyenne pour la prédiction)
future_scenarios = pd.DataFrame({
    'tos': future_temperature['tos']  # Utilisez les températures futures pour la prédiction
})

# Prédictions pour les scénarios futurs
future_predictions = rf_model.predict(future_scenarios)

# Affichage des prédictions pour chaque année future
for i, scenario in enumerate(future_scenarios['tos']):
    print(f"Scénario {future_scenarios['tos'].iloc[i]}°C : Taux de production prévu = {future_predictions[i]:.2f}")

# Visualisation des prédictions pour les scénarios futurs
plt.figure(figsize=(10, 6))
plt.plot(future_scenarios['tos'], future_predictions, marker='o', color='skyblue')
plt.title("Prédictions du Taux de Production des Puffins selon les Scénarios de Température Future")
plt.xlabel("Température Océanique (°C)")
plt.ylabel("Taux de Production")
plt.grid(True)
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/future_predictions.png', dpi=300)
plt.show()

# Créer une visualisation avec le temps sur l'axe des x et le taux de production prédit sur l'axe des y
plt.figure(figsize=(10, 6))
plt.plot(future_scenarios['tos'], future_predictions, marker='o', linestyle='-', color='skyblue')

# Ajouter un titre, des labels pour les axes, et des options de formatage
plt.title("Prédictions du Taux de Production des Puffins selon les Scénarios de Température Future", fontsize=16)
plt.xlabel("Année (Température Océanique Prévue en °C)", fontsize=12)
plt.ylabel("Taux de Production des Puffins", fontsize=12)
plt.grid(True)

# Afficher la figure
plt.tight_layout()

# Sauvegarder la figure en PNG
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/predictions_in_time.png', dpi=300)

# Afficher la figure
plt.show()

# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt

# Supposons que vous avez les données de température pour les années futures dans `future_scenarios` 
# et que vous avez déjà entraîné votre modèle RandomForest (rf_model) pour faire des prédictions.

# Supposons que 'temperature' contient une série de températures pour les années de 2023 à 2049 (par exemple)
# Et que vous voulez prédire le taux de production pour chaque année en fonction des températures océaniques

# Exemple : création d'un DataFrame avec les températures futures pour les années 2023-2049
future_years = range(2023, 2050)  # Années futures
future_temperatures = X['tos'].mean() + np.arange(1, len(future_years) + 1)  # Scénarios de températures futures

# Créer un DataFrame avec ces scénarios de température pour chaque année future
future_scenarios = pd.DataFrame({
    'time': future_years,
    'tos': future_temperatures
})

# Prédictions pour ces années futures
future_predictions = rf_model.predict(future_scenarios[['tos']])

# Visualisation de la prédiction du taux de production des puffins dans le temps
plt.figure(figsize=(10, 6))
plt.plot(future_scenarios['time'], future_predictions, marker='o', linestyle='-', color='skyblue')

# Ajouter un titre et des étiquettes
plt.title("Prédictions du Taux de Production des Puffins selon les Scénarios de Température (2023-2049)", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Taux de Production des Puffins", fontsize=12)
plt.grid(True)

# Sauvegarder la figure
plt.tight_layout()
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/predictions_in_time_with_years.png', dpi=300)

# Afficher la figure
plt.show()