import pandas as pd

# Chemin vers le fichier CSV
fichier_csv = "/home/onyxia/work/projet_python_2024_ENSAE/glace_arctique.csv"

# Lire le fichier CSV
df = pd.read_csv(fichier_csv)

# Afficher les premières lignes du DataFrame
print(df.head())



# Chemin vers le fichier XML
fichier_xml = "/home/onyxia/work/projet_python_2024_ENSAE/SEAICE_ARC_SEAICE_L4_NRT_OBSERVATIONS_011_008.xml"

# Lire le fichier XML dans un DataFrame pandas
df = pd.read_xml(fichier_xml)

# Afficher les premières lignes du DataFrame
print(df.head())