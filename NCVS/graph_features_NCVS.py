import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

df = pd.read_csv('C:/Users/hp/Documents/Aug2022/303COM/database/Population_Victimization_1.csv')
df.columns = ['idper', 'year', 'ager', 'hincome', 'marital', 'locality', 'educatn', 'VAW']
df = df.drop('idper', axis = 1)

#education level
df = df[df['VAW'] == 1]
df['educatn'] = df['educatn'].map({1: 'No schooling', 2: 'Grade School', 3: 'Middle School', 4: 'Some High School', 5: 'High School Graduate',
                                   6: 'Some College & \n Associate Degree', 7: 'Bachelor`s Degree', 8: 'Advanced Degree', 98: 'Residue'})
g = sns.catplot(x='educatn',y='VAW', order=['No schooling', 'Grade School', 'Middle School', 'Some High School', 'High School Graduate',
                                            'Some College & \n Associate Degree', 'Bachelor`s Degree', 'Advanced Degree', 'Residue'],
                data=df,kind='bar',ci=None,palette = 'Pastel1', estimator=sum)
title = "Education Level"
plt.title(title)
plt.show()

#age
df = df[df['VAW'] == 1]
df['ager'] = df['ager'].map({1: '12-17', 2: '18-24', 3: '25-34', 4: '35-49', 5: '50-64',
                                   6: '65 or older'})
g = sns.catplot(x='ager',y='VAW', order=['12-17', '18-24', '25-34', '35-49', '50-64', '65 or older'],
                data=df,kind='bar',ci=None,palette = 'Pastel1', estimator=sum)
title = "Age Range"
plt.title(title)
plt.show()

#employment status
df = df[df['VAW'] == 1]
df['hincome'] = df['hincome'].map({1: 'Less than $25,000', 2:'$25,000 to $49,999', 3: '$50,000 to $99,999', 4: '$100,000 to $199,999', 5: '$200,000 or more'})
g = sns.catplot(x='hincome',y='VAW', order=['Less than $25,000', '$25,000 to $49,999', '$50,000 to $99,999' , '$100,000 to $199,999', '$200,000 or more'],
                data=df,kind='bar',ci=None,palette = 'Pastel1', estimator=sum)
title = "Income Status"
plt.title(title)
plt.show()

# #marital status
df = df[df['VAW'] == 1]
df['marital'] = df['marital'].map({1: 'Never married', 2: 'Married', 3: 'Widowed', 4: 'Divorced', 5: 'Separated', 88: 'Residue'})
g = sns.catplot(x='marital',y='VAW', order=['Never married', 'Married', 'Widowed', 'Divorced', 'Separated', 'Residue'],
                data=df,kind='bar',ci=None,palette = 'Pastel1', estimator=sum)
title = "Marital Status"
plt.title(title)
plt.show()

#residence
df = df[df['VAW'] == 1]
df['locality'] = df['locality'].map({1: 'Urban', 2: 'Suburban', 3: 'Rural'})
g = sns.catplot(x='locality',y='VAW', order=['Urban', 'Suburban', 'Rural'],
                data=df,kind='bar',ci=None,palette = 'Pastel1', estimator=sum)
title = "Residence Area"
plt.title(title)
plt.show()
