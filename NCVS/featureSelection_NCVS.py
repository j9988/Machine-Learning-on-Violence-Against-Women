import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LogisticRegression

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)
sns.set(font_scale=1.7)

data = pd.read_csv('C:/Users/hp/Documents/Aug2022/303COM/database/Population_Victimization_1.csv')
data.columns = ['idper', 'year', 'ager', 'hincome', 'marital', 'locality', 'educatn', 'VAW']
data = data.drop('idper', axis = 1)

model = LogisticRegression(random_state=1,solver='lbfgs', max_iter=1000)

#without value
print("feature importance without value")
data_x = data.drop('VAW', axis = 1)
data_x.columns = ['year', 'ager', 'hincome', 'marital', 'locality', 'educatn']
model.fit(data_x, data['VAW'])

feature_importance = pd.DataFrame(
    {'feature': list(data_x.columns), 'feature_importance': [abs(i) for i in model.coef_[0]]})
feature_importance.sort_values('feature_importance', ascending=False)

#ordering the data
feature_importance = feature_importance.sort_values('feature_importance', ascending = False)
print(feature_importance)

g = sns.catplot(x='feature',y='feature_importance',
                data=feature_importance,kind='bar',ci=None, palette = 'Pastel1')
title = "Feature Selection"
plt.title(title)
plt.show()
