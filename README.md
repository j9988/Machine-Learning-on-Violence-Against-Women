# Machine-Learning-on-Violence-Against-Women
## Introduction
Violence against women and girls is one of the most widespread, persistent, and damaging human rights abuses in the world today, owing to the impunity, silence, 
stigma, and shame that surrounds it (United Nations, n.d.). With the availability of data and the desire to reduce and prevent violence against women, data 
science algorithms have begun to be used in this field. To predict violence against women, this study Logistic Regression model, Random Forest model and Artificial Neural Network model were being used in this research. The research plan is divided into five major stages: data collection, data cleansing and feature selection, model training, and outcome evaluation and model deployment.

## Data Acquisition 
- Demographic and Health Surveys (**DHS**) Program dataset contributed by Andrew Maranhão who is a Senior Data Scientist at Hospital Albert Einstein, Brazil.
- National Crime Victimization Survey (**NCVS**) from Bureau of Justice Statistics (BJS) which is an official website from the United States government, Department of Justice.

## DHS Dataset
  
### Issues in DHS Dataset
- Data Contains Missing Value

### Data Cleansing for DHS Dataset
Data is skewed in the box plot. The missing values need to be replaced using **median** instead of mean since the presence of numerous or a significant number of outlier data points indicates that the data is skewed in box plot. It is not advised to replace missing values with the mean in these circumstances since outlier data points will significantly affect the mean.

### Feature Selection for DHS Dataset
> feature importancy graph to be include

### Model Training for DHS Dataset
#### 1. Random Forest
##### 1.1 Tuning
The best accuracy obtained via tuning was **0.057** when the n_estimators were set to 100, the max_features to 1, and the max_depth to 4. The same result was obtained by changing the n_estimators to 200, max_features to 1, and max_depth to 5, or n_estimators to 300, max_features to 1, and max_depth to 5 too. As a consequence, since all three produced the same highest result, the n_estimators were set to 100, max_features to 1, and max_depth to 4.
##### 1.2 Model Training
During the literature review step, 75% of the dataset was used as the training set and 25% as the testing set, which was shown to be the optimal combination. The random forest tuning in the previous section was used to obtain the n_estimators, max_features, and max_depth.
##### 1.3 Prediction Result 
- [x] Training Accuracy: 0.06095
- [x] Testing Accuracy: 0.05368

#### 2. Artificial Neural Network 
Neural networks with two hidden layers, can represent functions of any shape (Heaton, 2008). Thus, two hidden layers were being employed in this model. Whereas for the number of units, there were three rules to be followed. In practise, the researcher recommends experimenting with smaller batch sizes first (typically 32 or 64). To fully utilise the GPU's processing, the range of batch sizes should be a power of two (Kandel and Castelli, 2020). Thus, the batch size being used to train this model is 32. 
##### 2.1 Prediction Result 
- [x] Training Accuracy: 0.0051
- [x] Testing Accuracy: 0.0063

#### 3. Logistic Regression
As seen in the feature selection section, the number of iterations used to execute model training for the NCVS dataset has no effect on prediction accuracy. As a result, a maximum iteration of 10000 was set.
##### 3.1 Prediction Result 
- [x] Training Accuracy: 0.066
- [x] Testing Accuracy: 0.055

### Conclusion on Model Training for DHS Dataset
The target value was in percentage which means while using the models to predict data, a result of low accuracy will be found as there is too many target value. 

### Linear Regression Estimation for DHS Dataset
Since the accuracy of training the models using DHS dataset is very low, by reading through articles, studying on the coefficient estimate to view the hidden patterns in the dataset is suggested (Cassy, Natário and Martins, 2016).

For complex sampling like this dataset, likelihood ratio tests were used to confirm this strategy. Adjusting for other variables, women that experienced no education had the highest probability of being experienced violence against women while comparing to the other categories of education level. By looking at the coefficient estimate, it is able to conclude that the higher the education level of an individual, the lower the probability of the women to be experiencing violence. Whereas for the employment status, the coefficient estimate shows that the women who is being employed for kind has the highest probability of experiencing violence, followed by employed for cash and employed. On the other hand, women who does not married before had the lowest probability of experiencing 
violence against women, followed by the widowed, divorced, separated and lastly the married or living together category. The coefficient estimate also shows that the women who lives in rural area does have higher probability to experience violence compared to the women who lives in the urban area.

## NCVS Dataset
### Data Cleansing for NCVS Dataset
Since this project did not aim to study the type of crime experienced by women, thus, the experience of violence against women was being transformed into 0 or 1 and saved into the VAW feature column. The women that experienced in being a victim of violence was being labelled as 1 in the VAW feature, whereas 0 was labelled if the women do not experience any violence. Therefore, the NULL value in the “newoff” feature does not affect the model training process. To cleanse the dataset that was going to be used for the model training, the “newoff” feature was being removed after adding in the VAW feature column.

### Feature Selection for NCVS Dataset
> feature importancy graph to be include

### Model Training for NCVS Dataset
#### 1. Random Forest
##### 1.1 Tuning
The highest accuracy retrieved from the tuning was 0.687 by setting the n_estimators to 200, max_features to sqrt and max_depth to None. By replacing the max_features to log2 and remaining the other attributes the same, the result was 0.687 too. Thus, since both shown the same highest result, the n_estimators to 200, max_features to sqrt and max_depth to None settings was being used. 
##### 1.2 Model Training
During the literature review step, 75% of the dataset was used as the training set and 25% as the testing set, which was shown to be the optimal combination. The random forest tuning in the previous section was used to obtain the n_estimators, max_features, and max_depth.
##### 1.3 Prediction Result 
- [x] Training Accuracy: 0.78
- [x] Testing Accuracy: 0.68

#### 2. Artificial Neural Network
Similar to the ANN model used for the DHS dataset, the ANN model used to train NCVS dataset also consists of two hidden layers and use 32 as batch size. 
##### 2.1 Prediction Result 
- [x] Training Accuracy: 0.64
- [x] Testing Accuracy: 0.65

#### 3. Logistic Regression
Maximum iteration of 100 was being set since this number of iterations is both the stable value and the is able to produce the highest accuracy. 
##### 3.1 Prediction Result 
- [x] Training Accuracy: 0.64
- [x] Testing Accuracy: 0.64
