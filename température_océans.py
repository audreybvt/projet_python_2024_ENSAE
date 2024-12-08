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
dfxml = pd.read_xml(fichier_xml)

# Afficher les premières lignes du DataFrame
print(dfxml.head())

import pandas as pd
from bs4 import BeautifulSoup

# Exemple de DataFrame
data = {
    'language': ['en', 'fr', 'de'],
    'contentInfo': ['<content><title>Document 1</title><body>Details about content 1</body></content>', 
                    '<content><title>Document 2</title><body>Details about content 2</body></content>', 
                    '<content><title>Document 3</title><body>Details about content 3</body></content>'],
    'distributionInfo': ['<distribution><url>www.example.com</url></distribution>',
                         '<distribution><url>www.example.fr</url></distribution>',
                         '<distribution><url>www.example.de</url></distribution>']
}



# Nettoyer les colonnes contentInfo et distributionInfo pour enlever les balises XML
dfxml['cleaned_content'] = df['contentInfo'].apply(lambda x: BeautifulSoup(x, 'html.parser').get_text() if isinstance(x, str) else x)
dfxml['cleaned_distribution'] = df['distributionInfo'].apply(lambda x: BeautifulSoup(x, 'html.parser').get_text() if isinstance(x, str) else x)

# Afficher le DataFrame avec des colonnes nettoyées
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)  # Limiter à 100 caractères
print(dfxml[['language', 'cleaned_content', 'cleaned_distribution']])
