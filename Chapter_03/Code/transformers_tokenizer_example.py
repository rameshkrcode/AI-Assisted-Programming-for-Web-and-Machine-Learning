
from transformers import AutoTokenizer

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize a sentence
tokens = tokenizer.tokenize("Write a Python function")
print("Tokens:", tokens)

# Convert tokens back to text
detokenized_text = tokenizer.convert_tokens_to_string(tokens)
print("Detokenized Text:", detokenized_text)
