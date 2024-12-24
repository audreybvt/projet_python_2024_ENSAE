from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger les données NetCDF (températures)
nc_file = "output/annual_mean_SST.nc"
data = xr.open_dataset(nc_file)

# Moyenne annuelle des températures
temperature = data['tos'].resample(time="1Y").mean().to_dataframe()
temperature.reset_index(inplace=True)

# Conversion des dates pour 'temperature'
temperature['time'] = pd.to_datetime(temperature['time'].astype(str))
temperature['time'] = temperature['time'].dt.year.astype('int64')

# Charger les données CSV (taux de production de puffins)
puffins = pd.read_csv("data/puffin-data1_Data.csv")
puffins.rename(columns={"Year": "time", "Prod": "production_rate"}, inplace=True)

# Joindre les données par année (colonne 'time')
merged_data = pd.merge(temperature, puffins[['time', 'production_rate']], on="time", how='inner')

# Vérifier et traiter les valeurs manquantes après la fusion
merged_data.dropna(subset=['tos', 'production_rate'], inplace=True)

# Visualisation des données
plt.scatter(merged_data['tos'], merged_data['production_rate'])
plt.title("Température vs Taux de Production des Puffins")
plt.xlabel("Température (°C)")
plt.ylabel("Taux de Production")
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/visualisation_données.png', dpi=300)
plt.show()

# Créer une série temporelle à partir des données fusionnées
merged_data_sarimax = merged_data.set_index('time')
merged_data_sarimax = merged_data_sarimax[['tos', 'production_rate']]

# Paramètres de SARIMAX
p, d, q = 1, 1, 1
P, D, Q, s = 1, 1, 0, 12  # Cycle saisonnier annuel

# Ajuster un modèle SARIMAX
sarimax_model = SARIMAX(
    merged_data_sarimax['production_rate'],
    exog=merged_data_sarimax[['tos']],
    order=(p, d, q),
    seasonal_order=(P, D, Q, s),
    enforce_stationarity=False,
    enforce_invertibility=False
)

# Entraîner le modèle
sarimax_results = sarimax_model.fit(disp=False)
print(sarimax_results.summary())

# Prédictions in-sample
sarimax_in_sample_pred = sarimax_results.predict(
    start=merged_data_sarimax.index[0],
    end=merged_data_sarimax.index[-1],
    exog=merged_data_sarimax[['tos']]
)

# Calcul des métriques
sarimax_mse = mean_squared_error(merged_data_sarimax['production_rate'], sarimax_in_sample_pred)
print(f"SARIMAX Mean Squared Error (in-sample): {sarimax_mse:.2f}")

# Visualisation des prédictions
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

# Charger les données NetCDF pour les scénarios futurs
future_nc_file = "output/annual_mean_SST_scenariossp585.nc"
future_data = xr.open_dataset(future_nc_file)

# Moyenne annuelle des températures futures
future_temperature = future_data['tos'].resample(time="1Y").mean().to_dataframe()
future_temperature.reset_index(inplace=True)
future_temperature['time'] = pd.to_datetime(future_temperature['time'].astype(str))
future_temperature['time'] = future_temperature['time'].dt.year.astype('int64')

# Préparer les données exogènes futures
future_scenarios = future_temperature[['time', 'tos']]
future_scenarios.set_index('time', inplace=True)

# Vérifiez que les années futures s'alignent correctement
start_year = merged_data_sarimax.index.min()
end_year = future_scenarios.index.max()
full_time_range = pd.date_range(start=f"{start_year}", end=f"{end_year}", freq='Y')

# Étendre et interpoler les données pour aligner les exogènes futures
exog_full = pd.DataFrame({'time': full_time_range.year})
exog_full = exog_full.merge(future_scenarios.reset_index(), on='time', how='left')
exog_full['tos'] = exog_full['tos'].interpolate(method='linear')

# Prédictions futures
sarimax_future_pred = sarimax_results.predict(
    start=merged_data_sarimax.index[0],
    end=len(full_time_range) - 1,
    exog=exog_full[['tos']]
)

# Ajout des prédictions dans un DataFrame pour visualisation
prediction_df = pd.DataFrame({
    'time': full_time_range.year,
    'production_rate_predicted': sarimax_future_pred
})

# Visualisation des prédictions futures
plt.figure(figsize=(12, 6))
plt.plot(prediction_df['time'], prediction_df['production_rate_predicted'], label="Prédictions SARIMAX", color="orange")
plt.scatter(merged_data['time'], merged_data['production_rate'], label="Données Observées", color="blue")
plt.title("Prédictions Futures du Taux de Production des Puffins")
plt.xlabel("Année")
plt.ylabel("Taux de Production")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/sarimax_predictions.png', dpi=300)
plt.show()
