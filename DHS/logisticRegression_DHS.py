import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, r2_score, explained_variance_score, classification_report, log_loss
from math import sqrt

np.set_printoptions(formatter={'float_kind': ':f'.format})
sns.set(rc={'figure.figsize': (12, 10)})
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

# raw_Data = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/violence_data_ValueCleaned.csv')
# print(raw_Data)

# raw_Data = raw_Data.drop('Survey Year', axis = 1)
# raw_Data = raw_Data.drop('Country', axis = 1)
# raw_Data.drop(columns=raw_Data.columns[0], axis=1, inplace=True)
# print(raw_Data)
# features = pd.get_dummies(raw_Data[['Demographics Question','Demographics Response','Question']])
# data_DQ = raw_Data['Demographics Question']
# data_value = raw_Data['Value']
# print(features)
# data_DQ.reset_index(drop=True, inplace=True)
# features.reset_index(drop=True, inplace=True)
# features.reset_index(drop=True, inplace=True)
# new_data = pd.concat([features, data_value], axis=1, join='inner')
# print(new_data)

new_data = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/categorize/full.csv')
print(new_data)

#spilt the data
X = new_data.drop('Value', axis=1).values
y = new_data['Value'].values
y = y.astype(int)

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.75, test_size = 0.25)

#training the model
log_reg = LogisticRegression(solver = 'lbfgs', max_iter=10000)
log_reg.fit(X_train, y_train)

#predict - predict class labels for samples in X
log_reg.predict(X_train)
y_pred = log_reg.predict(X_train)
print(y_pred)

#predict_proba - probability estimate (issues)
pred_proba = log_reg.predict_proba(X_train)

#coef_ - coefficient of the features in the decision function
log_reg.coef_

#evaluating the model
#accuracy on train
print("The Training Accuracy is: ", log_reg.score(X_train, y_train))

#accuracy on test
print("The Testing Accuracy is: ", log_reg.score(X_test, y_test))

#confusion matrix
prediction_test = log_reg.predict(X=X_test)
cm = confusion_matrix(y_test, prediction_test)
cm_norm = cm/cm.sum(axis=1)[:, np.newaxis]
plt.figure()
f=sns.heatmap(cm_norm, annot=True)
plt.title('Confusion Matrix for Logistic Regression Model')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.show()