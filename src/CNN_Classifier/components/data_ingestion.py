import os
import zipfile
import gdown
from CNN_Classifier import logger
from CNN_Classifier.utils.common import get_size
from CNN_Classifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)-> str:
        """
        fetch data from URL
        :return:  log information

        """
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?export=download&id='
            gdown.download(prefix+file_id , zip_download_dir)

            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into data directory

        :return: None

        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as ziper:
            ziper.extractall(unzip_path)

