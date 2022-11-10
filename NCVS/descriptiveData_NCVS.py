import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

raw_data = pd.read_csv('C:/Users/hp/Documents/Aug2022/303COM/database/Population_Victimization_1.csv')

raw_data.columns = ['idper', 'year', 'ager', 'sex', 'hincome', 'marital', 'locality', 'educatn', 'newoff', 'VAW']

print(raw_data.head())
print("\n")

print(raw_data.describe(include='all'))

# count no. of lines
print("Number of lines:", len(raw_data))
print("\n")

for column in raw_data:
        unique_vals = np.unique(raw_data[column])
        nr_values = len(unique_vals)
        if nr_values < 36:
            print('The number of values for feature {} :{} -- {}'.format(column, nr_values, unique_vals))
        else:
            print('The number of values for feature {} :{}'.format(column, nr_values))
print("\n")

print(raw_data.isnull().sum())
print("\n")
print(raw_data.max())
print(raw_data.min())
print("\n")

features = pd.get_dummies(raw_data[['idper', 'year', 'ager', 'sex', 'hincome', 'marital', 'locality', 'educatn', 'newoff', 'VAW']])

print(features.describe(include='all'))
df = features.describe(include='all')
df.to_csv('C:/Users/hp/Downloads/violence_data.csv/descriptive_data_dataset2.csv')
