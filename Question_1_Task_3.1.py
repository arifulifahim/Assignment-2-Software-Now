from collections import Counter
import csv

# Read the text file
with open('extracted_text.txt', 'r') as file:
    text = file.read()

# Tokenize the words
words = text.split()

# Count the word frequencies
word_counts = Counter(words)

# Get the top 30 common words
top_30_words = word_counts.most_common(30)

# Write the top 30 words and their counts to a CSV file
with open('top_30_words.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])
    writer.writerows(top_30_words)

