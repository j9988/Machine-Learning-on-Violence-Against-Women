import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn.linear_model import LogisticRegression

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

data = pd.read_csv('C:/Users/hp/Downloads/violence_data.csv/violence_data_NoNull.csv')
print(data)
data = data[['Index', 'Country', 'Demographics Question', 'Demographics Response', 'Question', 'Survey Year','Value']]

model = LogisticRegression(random_state=1,solver='lbfgs', max_iter=10000 )

data = data.drop('Index', axis = 1)
data = data.drop('Survey Year', axis = 1)
data = data.drop('Demographics Response', axis = 1)
print(data)

features = pd.get_dummies(data[['Country','Demographics Question','Question','Value']])
data_value = data['Value']
print(data_value)

#--------------------
#print(data_value.to_numpy())
data_value = data_value.sort_values(ascending=True)
data_value = data_value.to_numpy()
# # Fit a normal distribution to
# # the data:
# # mean and standard deviation
mu, std = norm.fit(data_value)
#
# # Plot the histogram.
#alpha = opacity of the line
plt.hist(data_value, bins=[0, 10,20,30,40,50, 60, 70,80,90,100], density=True, alpha=0.6, color='skyblue')
#
# # Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
#
plt.plot(x, p, 'k', linewidth=2)
title = "Separate According to Range \n Fit Values: {:.2f} and {:.2f}".format(mu, std)
plt.title(title)
#
plt.show()

plt.hist(data_value, bins=10, density=True, alpha=0.6, color='skyblue')
#
# # Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
#
plt.plot(x, p, 'k', linewidth=2)
title = "Separate into 10 Groups \nFit Values: {:.2f} and {:.2f}".format(mu, std)
plt.title(title)
#
plt.show()