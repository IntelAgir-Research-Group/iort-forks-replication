from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import csv

def preprocess_text(text):
    # Tokenize the text into individual words
    tokens = word_tokenize(text)

    # Remove punctuation and convert to lowercase
    tokens = [word.lower() for word in tokens if word.isalpha()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Stemming using Porter stemmer
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    # Join the stemmed tokens back into a single string
    preprocessed_text = ' '.join(stemmed_tokens)

    return preprocessed_text


# Read the CSV file
input_filename = 'text_data.csv'  # Update with your file name
output_filename = 'clear_data.csv'  # Update with your output file name

with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        # Assuming the text is in the first column of each row
        text = row['description']
        preprocessed_text = preprocess_text(text)
        writer.writerow([preprocessed_text])
        #print(preprocessed_text)