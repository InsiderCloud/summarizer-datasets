from Cogniezer.components.data_ingestion import DataIngestion
from Cogniezer.config.configuration import ConfigurationManager
from Cogniezer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            config_manager = ConfigurationManager()
            data_ingestion_config = config_manager.get_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.unzip_data()
