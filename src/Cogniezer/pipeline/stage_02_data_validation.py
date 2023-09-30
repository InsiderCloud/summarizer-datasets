from Cogniezer.components.data_validation import DataValidation
from Cogniezer.config.configuration import ConfigurationManager


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files()
