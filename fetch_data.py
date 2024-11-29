import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()

data_dir = './data'
os.makedirs(data_dir, exist_ok=True)

api.dataset_download_files("shalfey/extended-crab-age-prediction", path=data_dir)

import zipfile

zip_file_path = os.path.join(data_dir, "extended-crab-age-prediction.zip")
if os.path.exists(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)

print("Dane pobrane i rozpakowane!")
