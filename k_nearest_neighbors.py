# -*- coding: utf-8 -*-
"""k-nearest_neighbors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11wgL3ij5nViUvYCOVzs0UjDV-EYn6BA7

Start 13

# Classification - K-Nearest Neighbors
K = number of closest neighbors you want to test
You usually want K to be an odd number so there's no tie votes

-This works for two groups, but if you're trying to decide between three groups, 3 can evenly split 3 so you would use 5, keep this idea in mind as you choose K
# Perhaps using a modulus of sorts would be best for this.  A random number generator with modulus
If you match with something 2 out of 3 times that equals a 66% CONFIDENCE

-So Confidence is not accuracy, but confidence rating of your choice

#Euclidean Distance - Find the distance between the point in question and all other points

    - You then select the K number of shortest
    - This is computationally heavy
    - You can't train this algorithm - it's running the calculation on all the points every time
    - Can be calculated on up to a GB of data quickly

# SVM (Support Vector Machine) is much more efficient for Classification


 Start 14

 datasets = archive.ics.uci.edu/ml/datasets.php
"""

# K Nearest Neighbors

import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import cross_validate
import pandas as pd
from sklearn.model_selection import train_test_split


# Upload csv to github and 
url = 'https://raw.githubusercontent.com/morganbenavidez/Datasets/main/breast-cancer-wisconsin.data'

# Create dataframe
df = pd.read_csv(url)

# We know we have missing data, so we replace
df.replace('?', -99999, inplace=True)

# Drop useless columns
df.drop(['id'], 1, inplace=True)

# This will drop everything that has missing values
#df.dropna(inplace=True)

# Features - Everything except for the class column
X = np.array(df.drop(['class'], 1))

# Labels
y = np.array(df['class'])

# Cross Validation - test_size = percent of data you will test one
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Classifier
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

# $$$ PICKLE $$$
# You could save this as a pickle at this point and test things on the pickle

# Accuracy
accuracy = clf.score(X_test, y_test)
print('accuracy: ' + str(accuracy))

# This is unique and not in the dataset, so we will use it to test
example_measures = np.array([[4,2,1,1,1,2,3,2,1], [4,2,1,2,2,2,3,2,1]])
#example_measures = example_measures.reshape(1,-1) # The first number is for one sample
#example_measures = example_measures.reshape(2,-1) # The first number is for two samples
example_measures = example_measures.reshape(len(example_measures),-1) # The first number is for any number of samples

# Testing on the classifier(clf)
# If it was saved in a pickle, I think you would just replace the clf with the pickle
prediction = clf.predict(example_measures)
print(prediction)