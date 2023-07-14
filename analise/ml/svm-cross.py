import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load the CSV file
data = pd.read_csv('your_csv_file.csv')

# Split the data into text and label
X = data['text_column']
y = data['label_column']

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Initialize the SVM model
svm = SVC()

# Perform cross-validation
scores = cross_val_score(svm, X, y, cv=5)  # Change cv value as needed

# Print the cross-validation scores
print("Cross-validation scores:", scores)
print("Average score:", scores.mean())
