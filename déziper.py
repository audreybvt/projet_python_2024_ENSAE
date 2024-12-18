import zipfile

# Chemin vers ton fichier ZIP
zip_path = "/home/onyxia/projet_python_2024_ENSAE/data/cds_output_vestmann_ssp1_2_6.zip"
output_dir = "/home/onyxia/projet_python_2024_ENSAE/data/cds_output_vestmann-ssp1_2_6"  # Dossier où extraire les fichiers

# Créer le dossier de sortie s'il n'existe pas
import os
os.makedirs(output_dir, exist_ok=True)

# Ouvrir et extraire le contenu du fichier ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(output_dir)  # Extraire tous les fichiers dans le dossier de sortie
    print("Fichiers extraits :", zip_ref.namelist())  # Liste des fichiers extraits
