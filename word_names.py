import os
import csv
from nltk.corpus import words
import nltk

# Download the words dataset if not already present
try:
    word_set = set(words.words())
except LookupError:
    nltk.download('words')
    word_set = set(words.words())

def is_english_word(name):
    # Convert to lowercase for checking
    return name.lower() in word_set

def process_names_files():
    # Store all names that are English words
    word_names = set()
    
    # Process each file in the names directory
    names_dir = 'names'
    for filename in os.listdir(names_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(names_dir, filename)
            
            with open(file_path, 'r') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if row:  # Check if row is not empty
                        name = row[0].strip()
                        if is_english_word(name):
                            word_names.add(name)
    
    # Write results to output file
    with open('word_names.txt', 'w') as outfile:
        for name in sorted(word_names):
            outfile.write(name + '\n')

if __name__ == "__main__":
    process_names_files()
