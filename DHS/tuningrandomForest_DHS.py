import numpy as np
import pandas as pd
import seaborn as sns
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

np.set_printoptions(formatter={'float_kind':'{:f}'.format})
sns.set(rc={'figure.figsize':(8,6)})
warnings.filterwarnings('ignore')

new_data = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/categorize/full.csv')
print(new_data)

#spilt raw data - hold-out validation
X = new_data.drop('Value', axis=1).values
y = new_data['Value'].values
y = y.astype(int)
print('X shape: {}'.format(np.shape(X)))
print('y shape: {}'.format(np.shape(y)))
print("X shape:")
print(X)
print("----------------------------------------------------------------------------------------")
print("y shape:")
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=0.25, random_state=0)

#tunning RF
from itertools import product
n_estimators = [100, 200, 300]
max_features = [1, 'sqrt', 'log2']
max_depths = [None, 2, 3, 4, 5]
for n, f,d in product(n_estimators, max_features, max_depths): #with product we can iterate through all possible combinations
    rf = RandomForestClassifier(n_estimators=n, criterion='entropy', max_features=f, max_depth=d, n_jobs=2, random_state=0)
    rf.fit(X_train, y_train)
    prediction_test = rf.predict(X=X_test)
    print('Classification accuracy on test set with n_estimators = {} max features = {} and max_depth = {}: {:.3f}'.
          format(n, f, d, accuracy_score(y_test, prediction_test)))

