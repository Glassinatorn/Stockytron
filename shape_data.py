import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout

"""
Function to format dataset into the correct order
"""
def create_dataset(df):
    x = []
    y = []
    for i in range(50, df.shape[0]):
        x.append(df[i-50:i, 0])
        y.append(df[i, 0])
    x = np.array(x)
    y = np.array(y)

    return x,y

"""
Create training sets
"""
def shape_dataset(scaler, df):
    dataset_train = np.array(df[:int(df.shape[0]*0.8)])
    dataset_train = scaler.fit_transform(dataset_train)
    dataset_train[:5]

    dataset_test = np.array(df[int(df.shape[0]*0.8)-50:])
    dataset_test = scaler.transform(dataset_test)
    dataset_test[:5]

    x_train, y_train = create_dataset(dataset_train)
    x_train[:1]

    x_test, y_test = create_dataset(dataset_test)
    x_test[:1]

    # Reshape features for LSTM Layer
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    return x_train,y_train,x_test,y_test

"""
Function which builds and returns a lstm model
"""
def lstm_model(x_train, drop, units, layers):
    model = Sequential()
    model.add(LSTM(units, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(drop))

    for _ in range (0, (layers - 1)):
        model.add(LSTM(units, return_sequences=True))
        model.add(Dropout(drop))
    #model.add(LSTM(units=96, return_sequences=True))
    #model.add(Dropout(0.2))

    model.add(LSTM(units))
    model.add(Dropout(drop))
    model.add(Dense(units=1))

    return model
