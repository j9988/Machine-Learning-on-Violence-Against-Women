import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

df = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/violence_data_NoNull.csv')
df = df[['Country','Demographics Question','Demographics Response','Question','Survey Year','Value']]

#education level
graph_education = df[df['Demographics Question'] == 'Education']
graph_education = graph_education.drop('Demographics Question', axis = 1)
graph_education = graph_education.rename(columns={'Demographics Response': 'Education Level'})

g = sns.catplot(x='Education Level',y='Value',hue='Question',
                order=['No education','Primary','Secondary', 'Higher'],
                data=graph_education,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Education Level','Percentage (%)')
title = "Education Level"
plt.title(title)
plt.show()

g = sns.catplot(x='Education Level',y='Value',
                order=['No education','Primary','Secondary', 'Higher'],
                data=graph_education,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Education Level','Percentage (%)')
title = "Education Level"
plt.title(title)
plt.show()

#age
graph_age = df[df['Demographics Question'] == 'Age']
graph_age = graph_age.drop('Demographics Question', axis = 1)
graph_age = graph_age.rename(columns={'Demographics Response': 'Age Range'})

g = sns.catplot(x='Age Range',y='Value',hue='Question',
                order=['15-24','25-34','35-49'],
                data=graph_age,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Age Range','Percentage (%)')
title = "Age Range"
plt.title(title)
plt.show()

g = sns.catplot(x='Age Range',y='Value',
                order=['15-24','25-34','35-49'],
                data=graph_age,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Age Range','Percentage (%)')
title = "Age Range"
plt.title(title)
plt.show()

#employment status
graph_employment = df[df['Demographics Question'] == 'Employment']
graph_employment = graph_employment.drop('Demographics Question', axis = 1)
graph_employment = graph_employment.rename(columns={'Demographics Response': 'Employment Status'})

g = sns.catplot(x='Employment Status',y='Value',hue='Question',
                order=['Unemployed','Employed for kind','Employed for cash'],
                data=graph_employment,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Employment Status','Percentage (%)')
title = "Employment Status"
plt.title(title)
plt.show()

g = sns.catplot(x='Employment Status',y='Value',
                order=['Unemployed','Employed for kind','Employed for cash'],
                data=graph_employment,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Employment Status','Percentage (%)')
title = "Employment Status"
plt.title(title)
plt.show()

#marital status
graph_marital = df[df['Demographics Question'] == 'Marital status']
graph_marital = graph_marital.drop('Demographics Question', axis = 1)
graph_marital = graph_marital.rename(columns={'Demographics Response': 'Marital Status'})

g = sns.catplot(x='Marital Status',y='Value',hue='Question',
                order=['Never married','Widowed, divorced, separated','Married or living together'],
                data=graph_marital,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Marital Status','Percentage (%)')
title = "Marital Status"
plt.title(title)
plt.show()

g = sns.catplot(x='Marital Status',y='Value',
                order=['Never married','Widowed, divorced, separated','Married or living together'],
                data=graph_marital,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Marital Status','Percentage (%)')
title = "Marital Status"
plt.title(title)
plt.show()

#residence
graph_residence = df[df['Demographics Question'] == 'Residence']
graph_residence = graph_residence.drop('Demographics Question', axis = 1)
graph_residence = graph_residence.rename(columns={'Demographics Response': 'Residence Area'})

g = sns.catplot(x='Residence Area',y='Value',hue='Question',
                order=['Rural','Urban'],
                data=graph_residence,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Residence Area','Percentage (%)')
title = "Residence Area"
plt.title(title)
plt.show()

g = sns.catplot(x='Residence Area',y='Value',
                order=['Rural','Urban'],
                data=graph_residence,kind='bar',ci=None, palette = 'Pastel1')
g.set_axis_labels('Residence Area','Percentage (%)')
title = "Residence Area"
plt.title(title)
plt.show()