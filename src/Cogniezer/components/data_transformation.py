import os
from typing import Any
from Cogniezer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from Cogniezer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
   
    def convert_examples_to_features(self, batch):
        # Tokenize contexts and questions (as pairs of inputs)
        inputs = self.tokenizer(batch["dialogue"], max_length=4096, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target = self.tokenizer(batch["summary"], max_length=512, truncation=True)

        return {
            "input_ids": inputs.input_ids,
            "attention_mask": inputs.attention_mask,
            "labels": target.input_ids,
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))