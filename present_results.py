import numpy as np
import matplotlib.pyplot as plt

"""
Function to show the predictions in form of a graph
"""
def create_graph(df, y_train, y_test, scaler, predictions):
    fig, ax = plt.subplots(figsize=(8,4))
    plt.plot(df, color='red',  label="True Price")
    ax.plot(range(len(y_train)+50,len(y_train)+50+len(predictions)),predictions, color='blue', label='Predicted Testing Price')
    plt.legend()
    plt.savefig('tmp.png')

    # show focused prediction graph
    y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(y_test_scaled, color='red', label='True Testing Price')
    plt.plot(predictions, color='blue', label='Predicted Testing Price')
    plt.legend()
    plt.savefig('tmp3.png')


"""
Function to build a array of predictions to act upon
"""
def create_predictions(x_test, model, scaler):
    # printing predictions
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
