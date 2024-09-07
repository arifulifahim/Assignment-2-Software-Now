from transformers import AutoTokenizer
from collections import Counter



# Read the text file
with open('extracted_text.txt', 'r') as file:
    text = file.read()

# Load the BioBERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# Tokenize the text
tokens = tokenizer.tokenize(text)

# Count the unique tokens
token_counts = Counter(tokens)
top_30_tokens = token_counts.most_common(30)

# Print or store the top 30 tokens
print(top_30_tokens)

