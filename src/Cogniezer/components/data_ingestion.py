import os
from pathlib import Path
import urllib.request as request
import zipfile
from Cogniezer.entity import DataIngestionConfig
from Cogniezer.utils.common import get_size
from Cogniezer.logging import logger

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file)
            logger.info(f"Downloaded file {filename} with headers :\n{headers}")
        else:
            logger.info(f"File already exist of size {get_size(Path(self.config.local_data_file))}")

    def unzip_data(self):
        unzip_path = self.config.unzip_dir
        if not os.path.exists(unzip_path):
            os.makedirs(unzip_path)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)