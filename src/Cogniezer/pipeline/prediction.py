from transformers import pipeline
from transformers import AutoTokenizer
from Cogniezer.config.configuration import ConfigurationManager
from Cogniezer.logging import logger

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.config_manager=self.config.get_model_evaluation_config()
    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config_manager.tokenizer_path)
        gen_kwargs = {"length_penalty":0.8,"num_beams":8,"max_length":512}
        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

        logger.info("Generating summary")
        logger.info(f"Input Text: {text}")
        
        summary = pipe(text, **gen_kwargs)[0]['summary_text']
        
        logger.info(f"Generated Summary: {summary}")
        return summary