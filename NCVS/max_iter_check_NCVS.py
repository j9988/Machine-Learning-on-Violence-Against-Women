import pandas as pd
import sklearn
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import numpy as np

print(sklearn.__version__)

data = pd.read_csv('C:/Users/hp/Documents/Aug2022/303COM/database/Population_Victimization_1.csv')

data.columns = ['idper', 'year', 'ager', 'hincome', 'marital', 'locality', 'educatn', 'VAW']

model = LogisticRegression(random_state=1,solver='lbfgs', max_iter=100000)

# Create a template lit to store accuracies
acc = []
X = data.drop('VAW', axis=1).values
y = data['VAW'].values

# split into train test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25)

# Iterate along a logarithmically spaced ranged
for i in np.logspace(0,5, num = 6):
    # Print out the number of iterations to use for the current loop
    print('Training model with iterations: ', i)
    model_iter = LogisticRegression(random_state=1, solver='lbfgs', max_iter=i, class_weight='balanced')
    # Fit the algorithm to the data
    model_iter.fit(X_train, Y_train)
    # Append the current accuracy score to the template list
    acc.append(accuracy_score(Y_test, model_iter.predict(X_test)) * 100)

# Convert the accuracy list to a series
acc = pd.Series(acc, index = np.logspace(0,5, num = 6))
# Set the plot size
plt.figure(figsize = (15,10))
# Set the plot title
title = 'Graph to show the accuracy of the logistic regression model as number of iterations increases\nfinal accuracy: ' + str(acc.iloc[-1])
plt.title(title)
# Set the xlabel and ylabel
plt.xlabel('Number of iterations')
plt.ylabel('Accuracy score')
# Plot the graph
acc.plot.line()
plt.show()

print(acc)
