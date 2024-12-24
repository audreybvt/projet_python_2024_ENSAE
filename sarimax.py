from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

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

plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/visualisation_données.png', dpi=300)
plt.show()

'''
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
'''

# Créer une série temporelle à partir des données fusionnées
# Utilisez 'time' comme index et 'production_rate' comme série cible
merged_data_sarimax = merged_data.set_index('time')
merged_data_sarimax = merged_data_sarimax[['tos', 'production_rate']].dropna()

# Paramètres de SARIMAX : p, d, q, P, D, Q, s (cycle saisonnier)
# Ici, nous choisissons s=12 (annuel), ajustez selon les données
p, d, q = 1, 1, 1
P, D, Q, s = 1, 1, 0, 12  # Si la saisonnalité est importante

# Ajuster un modèle SARIMAX en utilisant la température comme variable explicative (exogène)
sarimax_model = SARIMAX(
    merged_data_sarimax['production_rate'],  # Variable dépendante
    exog=merged_data_sarimax[['tos']],       # Variable explicative (température)
    order=(p, d, q),
    seasonal_order=(P, D, Q, s),
    enforce_stationarity=False,
    enforce_invertibility=False
)

# Entraîner le modèle
sarimax_results = sarimax_model.fit(disp=False)

# Afficher le résumé du modèle
print(sarimax_results.summary())

# Prédictions in-sample (sur les données d'entraînement)
sarimax_in_sample_pred = sarimax_results.predict(
    start=merged_data_sarimax.index[0],
    end=merged_data_sarimax.index[-1],
    exog=merged_data_sarimax[['tos']]
)

# Calcul des métriques d'évaluation
sarimax_mse = mean_squared_error(merged_data_sarimax['production_rate'], sarimax_in_sample_pred)
print(f"SARIMAX Mean Squared Error (in-sample): {sarimax_mse:.2f}")

# Visualisation des résultats in-sample
plt.figure(figsize=(12, 6))
plt.plot(merged_data_sarimax.index, merged_data_sarimax['production_rate'], label='Taux Observé')
plt.plot(merged_data_sarimax.index, sarimax_in_sample_pred, label='Prédictions SARIMAX', color='orange')
plt.title("Prédictions In-Sample avec SARIMAX")
plt.xlabel("Année")
plt.ylabel("Taux de Production")
plt.legend()
plt.grid(True)
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/sarimax_insample.png', dpi=300)
plt.show()

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

# 1. Générer une plage temporelle complète pour les prédictions
start_year = merged_data['time'].min()  # Première année des données
end_year = future_temperature['time'].max()  # Dernière année pour les prévisions
full_time_range = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq='Y')

# Vérifier la forme attendue des données exogènes (dans ce cas, température 'tos')
expected_shape = len(full_time_range)

# 2. Étendre les données exogènes pour couvrir toute la plage de temps
# Vérifiez si des années manquent et remplissez-les avec une estimation ou interpolation
exog_full = pd.DataFrame({'time': full_time_range.year})
exog_full = exog_full.merge(merged_data[['time', 'tos']], on='time', how='left')

# Interpolation pour les années manquantes
exog_full['tos'] = exog_full['tos'].interpolate(method='linear')

# 3. Vérifiez la forme finale
print(f"Forme finale des données exogènes : {exog_full.shape}")

# 4. Effectuer des prédictions
sarimax_in_sample_pred = sarimax_results.predict(
    start=0,  # Début des prédictions
    end=len(full_time_range) - 1,  # Fin des prédictions
    exog=exog_full[['tos']]  # Exogènes alignées avec la plage temporelle
)

# 5. Ajouter les prédictions dans un DataFrame pour visualisation
prediction_df = pd.DataFrame({
    'time': full_time_range.year,
    'production_rate_predicted': sarimax_in_sample_pred
})

# Visualisation
plt.figure(figsize=(12, 6))
plt.plot(prediction_df['time'], prediction_df['production_rate_predicted'], label="Prédictions SARIMAX", color="orange")
plt.scatter(merged_data['time'], merged_data['production_rate'], label="Données observées", color="blue")
plt.title("Prédictions SARIMAX du Taux de Production des Puffins")
plt.xlabel("Année")
plt.ylabel("Taux de Production")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/sarimax_predictions.png', dpi=300)
plt.show()
'''
# Prédictions out-of-sample (sur des années futures)
future_exog = future_temperature[['tos']].dropna()
sarimax_forecast = sarimax_results.predict(
    start=future_temperature['time'].min(),
    end=future_temperature['time'].max(),
    exog=future_exog
)

# Visualiser les prédictions futures
plt.figure(figsize=(12, 6))
plt.plot(future_temperature['time'], sarimax_forecast, label='Prédictions Futures SARIMAX', color='green')
plt.title("Prédictions du Taux de Production des Puffins selon SARIMAX")
plt.xlabel("Année")
plt.ylabel("Taux de Production")
plt.legend()
plt.grid(True)
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/sarimax_prediction.png', dpi=300)
plt.show()
'''