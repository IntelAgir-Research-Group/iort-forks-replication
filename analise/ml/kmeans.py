import numpy as np
import nltk
from nltk.cluster import KMeansClusterer
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

# Read the CSV file
input_filename = 'clear_data.csv'  # Update with your output file name

with open(input_filename, 'r') as input_file:
    reader = csv.reader(input_file)
    corpus = []
    for row in reader:
        # Assuming the preprocessed text is in the first column of each row
        text = row[0]
        corpus.append(text)

# Prepare data for clustering
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
tfidf_matrix = np.asarray(tfidf_matrix.toarray())

# Perform clustering with K-means
num_clusters = 5  # Update with the desired number of clusters
clusterer = KMeansClusterer(num_clusters, distance=nltk.cluster.util.cosine_distance, repeats=25, avoid_empty_clusters=True)
clusters = clusterer.cluster(tfidf_matrix, assign_clusters=True)

# Print the cluster assignments
for i, cluster_id in enumerate(clusters):
    print(f"Text: {corpus[i]} | Cluster: {cluster_id}")