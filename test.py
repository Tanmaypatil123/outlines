import torch
from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')

model_l = torch.load(r"C:\Users\patil\Desktop\Modelshub\outlines\content\model.pt")
tokenizer_l = torch.load(r"C:\Users\patil\Desktop\Modelshub\outlines\content\tokenizer.pt")