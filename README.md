# Machine-Learning-on-Violence-Against-Women
## Introduction
Violence against women and girls is one of the most widespread, persistent, and damaging human rights abuses in the world today, owing to the impunity, silence, 
stigma, and shame that surrounds it (United Nations, n.d.). With the availability of data and the desire to reduce and prevent violence against women, data 
science algorithms have begun to be used in this field. To predict violence against women, this study Logistic Regression model, Random Forest model and Artificial Neural Network model were being used in this research. The research plan is divided into five major stages: data collection, data cleansing and feature selection, model training, and outcome evaluation and model deployment.

## Data Acquisition 
- Demographic and Health Surveys (**DHS**) Program dataset contributed by Andrew Maranhão who is a Senior Data Scientist at Hospital Albert Einstein, Brazil.

## DHS Dataset
  
### Issues in Dataset
- Data Contains Missing Value

### Data Cleansing
Data is skewed in the box plot. The missing values need to be replaced using **median** instead of mean since the presence of numerous or a significant number of outlier data points indicates that the data is skewed in box plot. It is not advised to replace missing values with the mean in these circumstances since outlier data points will significantly affect the mean.

### Feature Selection
> feature importance image to be include

### Model Training
#### 1. Random Forest
##### 1.1 Tuning
The best accuracy obtained via tuning was **0.057** when the n_estimators were set to 100, the max_features to 1, and the max_depth to 4. The same result was obtained by changing the n_estimators to 200, max_features to 1, and max_depth to 5, or n_estimators to 300, max_features to 1, and max_depth to 5 too. As a consequence, since all three produced the same highest result, the n_estimators were set to 100, max_features to 1, and max_depth to 4.
##### 1.2 Model Training
During the literature review step, 75% of the dataset was used as the training set and 25% as the testing set, which was shown to be the optimal combination. The random forest tuning in the previous section was used to obtain the n_estimators, max_features, and max_depth. 

#### 2. Artificial Neural Network 
Neural networks with two hidden layers, can represent functions of any shape (Heaton, 2008). Thus, two hidden layers were being employed in this model. Whereas for the number of units, there were three rules to be followed. In practise, the researcher recommends experimenting with smaller batch sizes first (typically 32 or 64). To fully utilise the GPU's processing, the range of batch sizes should be a power of two (Kandel and Castelli, 2020). Thus, the batch size being used to train this model is 32. 



