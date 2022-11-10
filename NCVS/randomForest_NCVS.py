import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

np.set_printoptions(formatter={'float_kind':'{:f}'.format})
sns.set(rc={'figure.figsize':(8,6)})
warnings.filterwarnings('ignore')

raw_data = pd.read_csv('C:/Users/hp/Documents/Aug2022/303COM/database/Population_Victimization_1.csv')
new_data = raw_data[["ager","hincome","marital","locality","educatn", "VAW"]]
print(new_data)

#spilt the data
X = new_data.drop('VAW', axis=1).values
y = new_data['VAW'].values
print('X shape: {}'.format(np.shape(X)))
print('y shape: {}'.format(np.shape(y)))

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=0.25, random_state=0)

#random forest
rf = RandomForestClassifier(n_estimators=200, criterion='entropy', max_features='sqrt', max_depth=None)
rf.fit(X_train, y_train)
prediction_test = rf.predict(X=X_test)

#accuracy on test
print("Training accuracy is: ", rf.score(X_train, y_train))
#accuracy on train
print("Testing accuracy is: ", rf.score(X_test, y_test))

#confusion matrix
cm = confusion_matrix(y_test, prediction_test)
cm_norm = cm/cm.sum(axis=1)[:, np.newaxis]
plt.figure()
f=sns.heatmap(cm_norm, annot=True)
plt.title('Confusion Matrix for Random Forest Model')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.show()

