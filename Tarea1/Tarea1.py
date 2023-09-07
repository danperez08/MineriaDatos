# Practica 1 - Descargar la dataset de internet

import kaggle
import zipfile

# Nos autenticamos en Kaggle con nuestra API key previamente guardada en el equipo
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

# Descargamos la dataset que más nos guste
# Lo que va entre las comillas simples primero va el nombre del usuario, después el nombre del dataset
# En "path" el ./ indica el directorio actual donde nos encontremos en la terminal
api.dataset_download_files("brunovr/metacritic-videogames-data", path="./")

# Se descargará la dataset en .zip, toca descomprimirlo
with zipfile.ZipFile(r"C:\Users\spide\OneDrive\Documents\Mineria\Tarea1\metacritic-videogames-data.zip", "r") as zipref:
    zipref.extractall("target/path")

# Y listo, ya tendriamos nuestro archivo listo para abrirlo y trabajar.