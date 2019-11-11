# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from math import floor
import math

df1 = pd.Series([2, 4, 5, 6, 7])
# print(df)
# print(df.tolist(), type(df))
df2 = pd.Series([1, 2, 4, 5, 6])
# print(df1+df2, df1-df2, df1*df2, df1/df2)

df = pd.DataFrame.from_dict([{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}])
# print(df) #convert from dict to dataframe put [] around

npArray = np.array([10, 20, 30, 40, 'a'])
# print(npArray)
toPdframe = pd.DataFrame(npArray)
# print(toPdframe)
toPdframe[0] = pd.to_numeric(toPdframe[0], errors='coerce')
#to convert all columns of dataframe 
df = toPdframe.apply(pd.to_numeric)
# print(df.fillna(0.0).astype(int)) #fill NAN values before applying conversion

data=[ [0, 1, 4, 7],
[1, 2, 5, 5],
[2, 3, 6, 8],
[3 ,4 ,9 ,12],
[4, 7, 5, 1],
[5, 11, 0, 11] ]
df = pd.DataFrame(data=data, columns=['col1', 'col2', 'col3', 'col4'])
# print(df.head(2))
df['col1'] = df['col1'].apply(pd.to_numeric)
# print(df['col1'])
#first column as series
df.ix[:,0] = df.ix[:, 0].apply(pd.to_numeric)
##use df.loc with column names or iloc with indexes for rows and columns access
df34 = pd.Series(df.ix[:,0])
# print(df34)
print(df.sum(axis=0, skipna=True))#sum each column, sum vertically
print(df.sum(axis=1, skipna=True)) #sum horizontally

# print(df)
# Write a Pandas program to convert Series of lists to one Series.
df0 = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
# print(df0.apply(pd.Series).stack().reset_index(drop=True))
# 0       Red
# 1     Green
# 2     White
# 3       Red
# 4     Black
# 5    Yellow
# dtype: object    

# print(df.sort_values('col3', 'col2'))
# print(df.columns[3])
newseries = df0.append(pd.Series([1, 2, 3]))
# print(df0, newseries)
compseries = pd.Series(np.random.rand(20)) #generate random between 0 and 1
# print(compseries[compseries<0.5]) #filtering rows - 1 method
# print(compseries.std(), compseries.mean())

df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
df['A'] = df['X'].apply(lambda row: row**3)
print(df)


exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=exam_data, index=labels)
print(df.info())
print(df.iloc[:, 0:2].to_string(index=False, header=False))

df0 = pd.DataFrame(data=[
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']]).fillna(' ')

df0.applymap(str.upper) #for entire datafram
# df0.iloc[0].apply(str.upper)












