# importing needed libraries and wrapping functions in other files
import os
from shape_data import *
from present_results import *
from gather_data import *


# getting the data
df = pd.read_csv('AAPL.csv')
df.head()
df = df['Open'].values
df = df.reshape(-1, 1)
df[:5]

# TODO: gather tokens and data
# tokens = get_tokens('.tokens')
# print(get_data('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'))

# formatting the data into seperate training andtesting sets
scaler = MinMaxScaler(feature_range=(0,1))
x_train,y_train,x_test,y_test = shape_dataset(scaler, df)

# build model if one is not available
if(not os.path.exists('saved_model')):
    model = lstm_model(x_train, 0.2, 96, 4)
    model.compile(loss='mean_squared_error', optimizer='adam')

    model.fit(x_train, y_train, epochs=100, batch_size=32)

    #model.save('model.h5')
else:
    model = load_model('model.h5')

# test the model
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

print_graph(df, y_train, y_test, scaler, predictions)
print(print_predictions(x_test, model, scaler))
