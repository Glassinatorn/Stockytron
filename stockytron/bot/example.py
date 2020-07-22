# importing needed libraries and wrapping functions in other files
import os
import numpy
from shape_data import *
from present_results import *
from gather_data import *

# creating a scaler to scale inputs
scaler = MinMaxScaler(feature_range=(0,1))



# getting the data
df = pd.read_csv('../data/AAPL.csv')
df.head()

df = df["Open"].values
df = df.reshape(-1, 1)
df[:5]


# formatting the data into seperate training andtesting sets
x_train,y_train,x_test,y_test = shape_dataset(scaler, df)

# build model if one is not available
if(not os.path.exists('../data/saved_model.h5')):
    model = gru_model(x_train, 0.01, 96, 4)
    model.compile(loss='mean_squared_error', optimizer='adam')

    model.fit(x_train, y_train, epochs=400, batch_size=64)

    model.save('../data/saved_model.h5')
else:
    model = load_model('../data/saved_model.h5')

# test the model
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

create_graph(df, y_train, y_test, scaler, predictions, "Close")
#print(create_predictions(x_test, model, scaler))

mean_y_test = y_test.mean()
mean_y_pred = create_predictions(x_test, model, scaler)
accuracy = (mean_y_test / mean_y_pred)
mean = 0
for _ in range(100):
    mean += accuracy[_]
mean = mean/100
print("Average distance:" + str(mean))


###########################################

         #testing source and tokens

###########################################
# tokens = get_file("../data/.tokens.json")
# sources = get_file("../data/.sources.json")
# all_data = get_all(tokens, sources)
# print(all_data)

###########################################

        #testing creating database

###########################################

#print(get_file("../data/AAPL.csv"))
