import pandas as pd
import fiona


# Lire les attributs (données tabulaires) à partir du fichier Shapefile
with fiona.open("/home/onyxia/projet_python_2024_ENSAE/redlist_species_data_321db943-1ccf-41f1-89a0-39c861e3e0ae/data_0.shp") as shapefile:
    # Extraire les données attributaires dans une liste de dictionnaires
    attributes = [feature["properties"] for feature in shapefile]

# Convertir les données attributaires en un DataFrame pandas
df = pd.DataFrame(attributes)

# Sélectionner les colonnes pertinentes (données temporelles et numériques)
columns_of_interest = ["YRCOMPILED", "ASSESSMENT", "SCI_NAME", "LEGEND"]  # Ajustez selon vos besoins
df_selected = df[columns_of_interest]

# Chemin pour enregistrer le fichier CSV
csv_output_path = "/home/onyxia/projet_python_2024_ENSAE/IUCN_data.csv"

# Sauvegarder les données sélectionnées dans un fichier CSV
df_selected.to_csv(csv_output_path, index=False)

print(f"Fichier CSV écrit avec succès à : {csv_output_path}")
