
from transformers import AutoTokenizer

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the word "unhappiness"
tokens = tokenizer.tokenize("unhappiness")
print(tokens)
