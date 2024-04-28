import torch
from basic_bert_unit.main import run_basic_model

if __name__ == '__main__':
    torch.set_default_dtype(torch.float16)
    run_basic_model()