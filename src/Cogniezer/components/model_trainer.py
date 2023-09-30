import os
from Cogniezer.entity import ModelTrainerConfig
from transformers import AutoTokenizer, Trainer, TrainingArguments
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
from datasets import load_dataset, load_from_disk
import torch
from Cogniezer.logging import logger

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config

    def train(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        logger.info(f"Using device: {device}")
        tokernizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer=tokernizer, model=model)

        train_dataset = load_from_disk(self.config.data_path)

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            save_steps=self.config.save_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps)

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset['test'],
            eval_dataset=train_dataset['validation'],
            data_collator=seq2seq_data_collator,
            tokenizer=tokernizer)

        trainer.train()

        trainer.save_model(os.path.join(self.config.root_dir, 'bigbird-samsum-model'))
        tokernizer.save_pretrained(os.path.join(self.config.root_dir, 'bigbird-samsum-tokenizer'))
