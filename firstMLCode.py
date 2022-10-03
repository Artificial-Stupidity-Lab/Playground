import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    '''Mean average error function'''
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

#file handler
melbourne_file_path = "C:/Users/mpilo/OneDrive - Durban University of Technology/Data_sets/Housing_Kaggle/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path) #reading to variable 
print(melbourne_data.columns) #displaying the columns
# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)
#Selecting the prediction target
y = melbourne_data.Price
#selecting the features (X)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

#quick review of data
print('\n',X.describe())
print('\n',X.head())
'''
#calculate missing data
nullsData = [
{'Rooms':melbourne_data.Rooms.isnull().sum(),'Bathroom':,'Landsize':,'Lattitude':,'Longitude':},
{'Rooms':,'Bathroom':,'Landsize':,'Lattitude':,'Longitude':}
]

nulls = pd.DataFrame(nullsData, index=["Missing Data Count","Missing Data %"])
print("\n",nulls)
'''
#prediction

# Define model. Specify a number for random_state to ensure same results each run
#spliting data for training and validation
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
melbourne_model = DecisionTreeRegressor(random_state=1)
# Fit model
melbourne_model.fit(train_X, train_y)
print("\nMaking predictions for the following 5 houses:")
print(train_X.head())
print("\nThe predictions are")
predictions_X = melbourne_model.predict(train_X.head())
print('\n', predictions_X)
#model validation
print('\nThe average error is : ', mean_absolute_error(val_y.head(), predictions_X))

# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("\nMax leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
print("\nFrom the results above, it can be seen that the best number of leaves is 500")   

#Random Forest
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(f'\nThe MEA using random forest is {mean_absolute_error(val_y, melb_preds)}')

#confirmation
print("\nCode Executed")