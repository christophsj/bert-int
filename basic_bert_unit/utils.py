from transformers import LlamaTokenizer, LlamaModel, BertTokenizer, BertModel
from enum import Enum

class Model(Enum):
    BERT = 1
    LLAMA = 2

llama_weights_path = '../llama'
bert_model = 'bert-base-multilingual-cased'
model = Model.BERT


def get_tokenizer():
   if model == Model.BERT:
        return BertTokenizer.from_pretrained(bert_model)
    
   return LlamaTokenizer.from_pretrained(llama_weights_path)

def get_model():
    if model == Model.BERT:
        return BertModel.from_pretrained(bert_model)
    
    return LlamaModel.from_pretrained(llama_weights_path)