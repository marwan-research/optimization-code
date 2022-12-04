# optimization-code
# -*- coding: utf-8 -*-
"""
Created on Fri dec  2 9:04:13 2022

@author: Malek
"""

import numpy 
import matplotlib.pyplot as plt
import pandas
import time
from sklearn.metrics import r2_score
from sklearn.metrics import r2_score
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import LabelEncoder
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from keras import models, layers
from sklearn.model_selection import train_test_split
numpy.random.seed(7)

df = pandas.read_excel('Time2.xlsx', usecols="A")
print(df)
df2 = df.values
df2 = df2.astype('float32')

print(df2)

def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)
look_back = 1
X, y = create_dataset(df2, look_back)

model = models.Sequential()
model.add(Dense(20, input_dim=1, kernel_initializer='normal', activation='relu'))
model.add(Dense(10,  activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))

# output layer
#model.add(layers.Dense(1))
model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])
history = model.fit(X, y, epochs=100)
y_pred = model.predict(X)
print('R:', r2_score(y, y_pred)) 
print('Mean Absolute Error:', metrics.mean_absolute_error(X, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(X, y_pred))  
print('result')
l = list(range(len(y_pred)))

plt.figure(figsize=(10, 8))
plt.plot(l, y, 'b-', label = 'Real values')
plt.plot(l, y_pred, 'r-', label = 'LSTM predictions')
plt.xlabel('Sample'); plt.ylabel('Demand'); plt.title('Prediction of the Uber demand using LSTM ')
plt.legend();
