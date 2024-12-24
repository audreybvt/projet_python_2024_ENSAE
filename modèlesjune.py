import xarray as xr
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Charger les données NetCDF pour les moyennes de SST de juin
nc_file_june = "output/june_mean_SST.nc"
data_june = xr.open_dataset(nc_file_june)

# Moyenne annuelle des températures pour juin
temperature_june = data_june['tos'].resample(time="1Y").mean().to_dataframe()
temperature_june.reset_index(inplace=True)

# Convertir la colonne 'time' en chaîne de caractères puis en datetime et en année
temperature_june['time'] = temperature_june['time'].astype(str)
temperature_june['time'] = pd.to_datetime(temperature_june['time'])
temperature_june['time'] = temperature_june['time'].dt.year.astype('int64')

# Charger les données CSV pour les taux de production des puffins
puffins = pd.read_csv("data/puffin-data1_Data.csv")

# Renommer la colonne 'Year' en 'time' pour correspondre à la colonne de température
puffins.rename(columns={"Year": "time", "Prod": "production_rate"}, inplace=True)

# Joindre les données par année
merged_data_june = pd.merge(temperature_june, puffins[['time', 'production_rate']], on="time", how='inner')

# Vérification des valeurs manquantes après la fusion
print(f"Nombre de lignes manquantes après fusion : {merged_data_june.isnull().sum().sum()}")

# Visualisation des données pour juin
plt.scatter(merged_data_june['tos'], merged_data_june['production_rate'])
plt.title("Température (Juin) vs Taux de Production des Puffins")
plt.xlabel("Température (°C)")
plt.ylabel("Taux de Production")
plt.show()

# Préparer les données pour le modèle
X_june = merged_data_june[['tos']]  # Température pour juin
y_june = merged_data_june['production_rate']  # Taux de production des puffins

# Supprimer les lignes où y est manquant
merged_data_june_clean = merged_data_june.dropna(subset=['production_rate', 'tos'])

# Vérification qu'il n'y a plus de NaN après le nettoyage
X_june_clean = merged_data_june_clean[['tos']]
y_june_clean = merged_data_june_clean['production_rate']

print("Valeurs manquantes après nettoyage dans y_june_clean :", y_june_clean.isnull().sum())

# Division en jeu d'entraînement et de test
X_train_june, X_test_june, y_train_june, y_test_june = train_test_split(X_june_clean, y_june_clean, test_size=0.2, random_state=42)

# Entraîner un modèle Random Forest
rf_model_june = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model_june.fit(X_train_june, y_train_june)

# Prédictions sur le jeu de test
y_pred_june = rf_model_june.predict(X_test_june)

# Évaluer la performance
mse_june = mean_squared_error(y_test_june, y_pred_june)
r2_june = r2_score(y_test_june, y_pred_june)
print(f"Mean Squared Error (Juin): {mse_june:.2f}")
print(f"R² Score (Juin): {r2_june:.2f}")

# Visualisation des prédictions
scatter = plt.scatter(y_test_june, y_pred_june, c=np.log1p(y_test_june), cmap='viridis', label='Taux de production', alpha=0.7)

# Ajouter un titre et des étiquettes
plt.title("Prédictions vs Observations (Random Forest - Juin)")
plt.xlabel("Observations")
plt.ylabel("Prédictions")

# Ajouter la barre de couleur pour la légende
cbar = plt.colorbar(scatter)
cbar.set_label('Valeur (log(y_test + 1))')

# Sauvegarder le graphique
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/prediction_observation_rf_june.png', dpi=300)
plt.show()

# Prédictions pour les scénarios futurs en juin
future_scenarios_june = pd.DataFrame({
    'tos': [X_june['tos'].mean() + 1, X_june['tos'].mean() + 2, X_june['tos'].mean() + 3]
})

# Prédictions pour les scénarios futurs
future_predictions_june = rf_model_june.predict(future_scenarios_june)

# Affichage des prédictions pour les scénarios
for i, scenario in enumerate(future_scenarios_june['tos']):
    print(f"Scénario {i+1} (Température = {scenario:.2f}°C) : Taux de production prévu = {future_predictions_june[i]:.2f}")

# Visualisation des prédictions pour les scénarios futurs
plt.figure(figsize=(10, 6))
plt.bar(['+1°C', '+2°C', '+3°C'], future_predictions_june, color='skyblue')
plt.title("Prédictions du Taux de Production des Puffins selon les Scénarios de Température en Juin")
plt.ylabel("Taux de Production")
plt.xlabel("Scénarios de Température")
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/predictions_june.png', dpi=300)
plt.show()
