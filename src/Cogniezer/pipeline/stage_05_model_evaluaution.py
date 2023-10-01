from Cogniezer.components import model_evaluation
from Cogniezer.config.configuration import ConfigurationManager


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = model_evaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()