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

# Visualiser les performances
plt.scatter(y_test, y_pred)
plt.title("Prédictions vs Observations (Random Forest)")
plt.xlabel("Observations")
plt.ylabel("Prédictions")

plt.savefig('/home/onyxia/work/projet_python_2024_ENSAE/output/prediction_observation_rf.png', dpi=300)
plt.show()

'''
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
        plt.show()
'''