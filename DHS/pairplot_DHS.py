import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

#df = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/only_full.csv')
#df = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/education_text.csv')
df = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/violence_data_NoNull_text.csv')
x = df

raw_Data = df
print(raw_Data.shape)
g = sns.pairplot(data = raw_Data, hue = 'Demographics Question', diag_kws={"shade": False, "linewidth": 2}, palette = 'Pastel1')
plt.show()

#investigate the distr of y
sns.countplot(x = 'Demographics Question', data = raw_Data, palette = 'Pastel1')
plt.show()