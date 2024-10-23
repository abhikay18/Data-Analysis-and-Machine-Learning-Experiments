import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

# Load the Iris data set
dataset = pd.read_csv("iris2.csv")  # Make sure to specify the correct path to your CSV file
print(dataset.shape)
print(dataset.head())
print(dataset.tail(2))
print(dataset.describe())

# Split the Iris features into input (X) and output (y)
X = dataset.iloc[:, 1:5].values  # Taking the 2nd to 5th columns as features
y = dataset.iloc[:, 5].values    # Taking the 6th column as the target (Species)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Train the model using KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)

# Predict the test set results
y_pred = classifier.predict(X_test)

# Evaluate the model using confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Print the accuracy score
accuracy = accuracy_score(y_test, y_pred) * 100
print(f'Accuracy of our model is equal to {accuracy:.2f}%.')

# Optionally, you can plot the results here using matplotlib
