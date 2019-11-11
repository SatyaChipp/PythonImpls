# Data Preprocessing Template

# Importing the libraries
import numpy as np ##mathtematical tools
import matplotlib.pyplot as plt
import pandas as pd #to import n manage datatsets

np.set_printoptions(threshold = np.nan) ##add this to get current output

## Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values#take columns except te last one
y = dataset.iloc[:, 3].values #last column

#replace missing data with mean -- one way to deal with missing data
from sklearn.preprocessing  import Imputer       #default mean          
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0) #axis 0 -means were taking mean of columns .. if 1 mean of rows                
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#encoding categorical data
np.set_printoptions(threshold = np.nan) ##add this to get current output

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_x = LabelEncoder() #encode labels with values 0 and nclasses-1
labelEncoder_x.fit_transform(X[:, 0]) #making the first of the matrix gets fitted with encoded values
X[:, 0] = labelEncoder_x.fit_transform(X[:, 0]) #making the first of the matrix gets fitted with encoded values
#num of classes in this data - 3 ==spain/germany/france
#encoded values are numerical 0, 1, 2 but ML algo might think 0,1,2 point to scores
#to solve this -- make dummy variables
#ith 3 new columns - as many as number of columns
oneHotEncoder = OneHotEncoder(categorical_features=[0]) #encode with one of k values
X = oneHotEncoder.fit_transform(X).toarray()

labelEncoder_y = LabelEncoder() #encode labels with values 0 and nclasses-1
y = labelEncoder_y.fit_transform(y) #making the first of the matrix gets fitted with encoded values
#encoded last column
 
#splitting dataset into traning and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) #dont give too muhc data for the test set
#train data -- to make ml model learn correlations in data
