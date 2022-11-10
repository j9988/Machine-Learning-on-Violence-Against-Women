from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

raw_data = pd.read_csv('C:/Users/hp/Documents/Aug2022/303COM/database/Population_Victimization_1.csv')
raw_data = raw_data[["ager","hincome","marital","locality","educatn", "VAW"]]
print(raw_data)

X = raw_data.drop('VAW', axis = 1).values
y = raw_data['VAW']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=0.25, random_state=0)
print(X_train.shape)

#Adding First Hidden Layer
ann = tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=9,activation="relu"))
 #Adding Second Hidden Layer
ann.add(tf.keras.layers.Dense(units=6,activation="relu"))
 #Adding Output Layer
ann.add(tf.keras.layers.Dense(units=1,activation="sigmoid"))
#Compiling ANN
ann.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])
#Fitting ANN
ann.fit(X_train,y_train,batch_size=32,epochs = 30, verbose=1)

print("Training Accuracy: ")
print(ann.evaluate(X_train,y_train))
print("Testing Accuracy: ")
print(ann.evaluate(X_test, y_test))