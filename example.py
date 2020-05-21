# importing needed libraries and wrapping functions in other files
import os
from shape_data import *
from present_results import *
from gather_data import *
from sklearn.model_selection import cross_val_score

# creating a scaler to scale inputs
scaler = MinMaxScaler(feature_range=(0,1))

to_test = ["Open","High","Low","Close","Adj","Volume"]

# getting the data
df = pd.read_csv('AAPL.csv')
df.head()
for column in to_test:
    df = df[column].values
    df = df.reshape(-1, 1)
    df[:5]

    # formatting the data into seperate training andtesting sets
    x_train,y_train,x_test,y_test = shape_dataset(scaler, df)

    # build model if one is not available
    if(not os.path.exists('saved_model')):
        model = lstm_model(x_train, 0.1, 96, 4)
        model.compile(loss='mean_squared_error', optimizer='adam')

        model.fit(x_train, y_train, epochs=100, batch_size=32)

        #model.save('model.h5')
    else:
        model = load_model('model.h5')

    # test the model
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)

    create_graph(df, y_train, y_test, scaler, predictions)
    print(create_predictions(x_test, model, scaler))
    mean_y_test = y_test.mean()
    mean_y_pred = create_predictions(x_test, model, scaler)
    accuracy = (mean_y_test / mean_y_pred) * 100, 2
    #print(accuracy)
