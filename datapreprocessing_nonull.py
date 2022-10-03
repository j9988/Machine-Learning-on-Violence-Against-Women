import pandas as pd
import numpy as np

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

df = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/violence_data_Copy.csv')
df = df[['Country','Demographics Question','Demographics Response','Question','Survey Year','Value']]

#education level
graph_education = df[df['Demographics Question'] == 'Education']
print("\n -----Education Null Value-----")
print(graph_education.isnull().sum())

graph_education['Value']=graph_education['Value'].fillna(graph_education['Value'].mean())
print(graph_education.isnull().sum())

#age
graph_age = df[df['Demographics Question'] == 'Age']
print("\n -----Age Null Value-----")
print(graph_age.isnull().sum())

graph_age['Value']=graph_age['Value'].fillna(graph_age['Value'].mean())
print(graph_age.isnull().sum())

#employment status
graph_employment = df[df['Demographics Question'] == 'Employment']
print("\n -----Employment Null Value-----")
print(graph_employment.isnull().sum())

graph_employment['Value']=graph_employment['Value'].fillna(graph_employment['Value'].mean())
print(graph_employment.isnull().sum())

#marital status
graph_marital = df[df['Demographics Question'] == 'Marital status']
print("\n -----Marital Null Value-----")
print(graph_marital.isnull().sum())

graph_marital['Value']=graph_marital['Value'].fillna(graph_marital['Value'].mean())
print(graph_marital.isnull().sum())

#residence
graph_residence = df[df['Demographics Question'] == 'Residence']
print("\n -----Residence Null Value-----")
print(graph_residence.isnull().sum())

graph_residence['Value']=graph_residence['Value'].fillna(graph_residence['Value'].mean())
print(graph_residence.isnull().sum())

data = pd.concat([graph_education,graph_age, graph_employment, graph_marital, graph_residence])
print(data.info())
data.to_csv('C:/Users/hp/Downloads/violence_data.csv/violence_data_NoNull.csv')


