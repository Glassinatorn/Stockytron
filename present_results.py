import numpy as np
import matplotlib.pyplot as plt

def create_graph(df, y_train, y_test, scaler, predictions, name):
    """
    A function to show the predictions in the form of a graph

    Parameters
    ----------
    df : array
        The dataset containing real prices.
    y_train : array
        Training dataset.
    y_test : array
        Validation dataset.
    scaler : MinMaxScaler
        A scaler to scale features between a min and max value.
    predictions : array
        Dataset containing the predicted prices.
    name : string
        The base name of the pictures.
    """
    fig, ax = plt.subplots(figsize=(8,4))
    plt.plot(df, color='black',  label="True Price")
    ax.plot(range(len(y_train)+50,len(y_train)+50+len(predictions)),predictions,
            color='green', label='Predicted Testing Price')
    plt.legend()
    plt.savefig(name+'_long.png')

    # show focused prediction graph
    y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(y_test_scaled, color='black', label='True Testing Price')
    plt.plot(predictions, color='green', label='Predicted Testing Price')
    plt.legend()
    plt.savefig(name+'_short.png')


def create_predictions(x_test, model, scaler):
    """
    Function to build a array of predictions to act upon.

    Parameters
    ----------
    x_test : array
        Training data.
    model : Sequential
        A model which has been trained.
    scaler : MinMaxScaler
        A scaler to scale features between a min and max value.

    Returns
    -------
    Preds: array
        Predictions for which to act upon.
    """
    x = x_test[-1]
    num_timesteps = 100
    preds = []
    for i in range(num_timesteps):
        data = np.expand_dims(x, axis=0)
        prediction = model.predict(data)
        prediction = scaler.inverse_transform(prediction)
        preds.append(prediction[0][0])
        x = np.delete(x, 0, axis=0) # delete first row
        x = np.vstack([x, prediction]) # add prediction

    return preds
