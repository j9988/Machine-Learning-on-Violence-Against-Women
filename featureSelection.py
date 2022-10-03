import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LogisticRegression

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

data = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/violence_data_NoNull.csv')
data = data[['Index', 'Country', 'Demographics Question', 'Demographics Response', 'Question', 'Survey Year','Value']]

model = LogisticRegression(random_state=1,solver='lbfgs', max_iter=10000 )

data = data.drop('Index', axis = 1)
data = data.drop('Survey Year', axis = 1)
data = data.drop('Demographics Response', axis = 1)

features = pd.get_dummies(data[['Country','Demographics Question','Question','Value']])
data['Value'] = data['Value'].astype(int)

#without value
print("feature importance without value")
features = features.drop('Value', axis = 1)
features.columns = ['Country', 'DQ_Age', 'DQ_Education', 'DQ_Employment   ', 'DQ_Marital status', 'DQ_Residence', 'Q_>=1 reasonn', 'Q_argues', 'Q_burns food', 'Q_goes out w/o telling', 'Q_neglects children', 'Q_refuses sex']
model.fit(features, data['Value'])

feature_importance = pd.DataFrame(
    {'feature': list(features.columns), 'feature_importance': [abs(i) for i in model.coef_[0]]})
feature_importance.sort_values('feature_importance', ascending=False)

#ordering the data
feature_importance = feature_importance.sort_values('feature_importance', ascending = False)
print(feature_importance)

g = sns.catplot(x='feature',y='feature_importance',
                data=feature_importance,kind='bar',ci=None, palette = 'Pastel1')
title = "Feature Selection"
plt.title(title)
plt.show()
