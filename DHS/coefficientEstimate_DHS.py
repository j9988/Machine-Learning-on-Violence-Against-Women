import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import statsmodels.api as sm
import scipy.stats as stats
import math

raw_data = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/categorize/education_text.csv')

raw_data = raw_data[raw_data['Demographics Response'] == 'Higher']
# raw_data = raw_data[raw_data['Question'] == "... for at least one specific reason" ]
raw_data = raw_data.drop('Question', axis = 1)

#raw_data = raw_data.drop('Demographics Response', axis = 1)
# print(raw_data)
value = raw_data[["Value"]]
full = pd.get_dummies(raw_data[["Question"]])
data_all = pd.concat([full, value], axis=1, join='inner')
print(data_all)
raw_data = data_all

#X = raw_data.drop('Value', axis = 1).values
X = raw_data.drop('Value', axis = 1)
y = raw_data['Value']

model_ = LinearRegression().fit(X, y)
r_sq = model_.score(X, y)
print(f"coefficient of determination: {r_sq}")

print(f"intercept: {model_.intercept_}")
print(f"slope: {model_.coef_}")

model = sm.OLS(y, X)
model2 = model.fit()
print(model2.summary())

