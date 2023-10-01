from Cogniezer.entity import ModelEvaluationConfig
from transformers import AutoModelSeq2SeqLM, AutoTokenizer
from datasets import load_metric, load_from_disk
import torch
import pandas as pd
from tqdm import tqdm

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def generate_batch_sized_chunks(self, data, batch_size):
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]

    def calculate_rouge_score(self,dataset,metric,tokenizer,
                batch_size=16,device='cuda' if torch.cuda.is_available() else 'cpu',
                column_text="article",column_summary="highlights"):
        
        article_batch= list(self.generate_batch_sized_chunks(dataset[column_text],batch_size))
        summary_batch= list(self.generate_batch_sized_chunks(dataset[column_summary],batch_size))

        for article_batch,summary_batch in tqdm(zip(article_batch,summary_batch),total=len(article_batch)):
            inputs = tokenizer(article_batch, padding="max_length",max_length=4096, truncation=True, return_tensors="pt")
            
            summaries = model.generate(input_ids=inputs.input_ids.to(device),
                                        attention_mask=inputs.attention_mask.to(device),
                                        max_length=256,
                                        num_beams=8,
                                        length_penalty=0.8,
                                        early_stopping=True)
            
            decode_summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in summaries]
            decode_summary = [d.replace('',' ') for d in decode_summary]

            metric.add_batch(predictions=decode_summary,references=summary_batch)

            score = metric.compute()
            return score
        
        def evaluate(self):
            device= 'cuda' if torch.cuda.is_available() else 'cpu'
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            model = AutoModelSeq2SeqLM.from_pretrained(self.config.model_path).to(device)

            dataset_pt = load_from_disk(self.config.data_path)

            rouge_names = ["rouge1","rouge2","rougeL","rougeLsum"]

            metric = load_metric("rouge")

            score = self.calculate_rouge_score(dataset_pt['test'][0:100],metric,model,tokenizer,batch_size=2,column_text="article",column_summary="highlights")

            rouge_dict = dict((rn, score[rn].mid.fmeasure * 100) for rn in rouge_names)

            df = pd.DataFrame(rouge_dict,index=['bigbird'])
            df.to_csv(self.config.metric_file_name,index=False)
