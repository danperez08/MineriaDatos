import kaggle
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

api.dataset_download_files("brunovr/metacritic-videogames-data", path="./")

with zipfile.ZipFile(r"C:\Users\spide\OneDrive\Documents\Mineria\Tarea1\metacritic-videogames-data.zip", "r") as zipref:
    zipref.extractall("target/path")

