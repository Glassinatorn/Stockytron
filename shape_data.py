import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout

def create_dataset(df):
    """
    Function to create datasets for prediction model.

    Parameters
    ----------
    df : array
        Data to be split into train data for prediction model.

    Returns
    -------
    x : array
       Train data for x-axis.
    y : array
       Train data for y-axis.
    """

    x = []
    y = []
    for i in range(50, df.shape[0]):
        x.append(df[i-50:i, 0])
        y.append(df[i, 0])
    x = np.array(x)
    y = np.array(y)

    return x,y


def shape_dataset(scaler, df):
    """
    Function to shape given data into train and validation data for prediction
    model.

    Parameters
    ----------
    scaler : MinMaxScaler
        A scaler to scale features between a min and max value.

    Returns
    -------
    x_train :  array
        Data to train and build a prediction model with.
    y_train :  array
        Data to train and build a prediction model with.
    x_test :  array
        Test data to validate the created prediction model with.
    y_test :  array
        Test data to validate the created prediction model with.
    """

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


def lstm_model(x_train, drop, units, layers):
    """
    Function to build a LSTM model with which to predict real-time series based
    on historical data.

    Parameters
    ----------
    x_train : array
        Training data with which to build and train the model.
    drop : int
        How much "knowledge" should be forgotten in each layer iteration of the
        model to combat overfitness.
    units : int
        How many units there should be in each layer of the model.
    layers : int
        How many layers the model should have to iterate.

    Returns
    -------
    model : Sequential
        A LSTM model that is ready to be trained.
    """

    model = Sequential()
    model.add(LSTM(units, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(drop))

    for _ in range (0, (layers - 1)):
        model.add(LSTM(units, return_sequences=True))
        model.add(Dropout(drop))

    model.add(LSTM(units))
    model.add(Dropout(drop))
    model.add(Dense(units=1))

    return model
