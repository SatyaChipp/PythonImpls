# -*- coding: utf-8 -*-

txt = '''450
 00:17:53,457 --> 00:17:56,175
 Okay, but, um,
 thanks for being with us.

451
 00:17:56,175 --> 00:17:58,616
 But, um, if there's any
 college kids watching,

452
 00:17:58,616 --> 00:18:01,610
 But, um, but, um, but, um,
 out, um, but, um,

453
 00:18:01,610 --> 00:18:03,656
 We have to drink, professor.
454
 00:18:03,656 --> 00:18:07,507
 It's the rules.
 She said "But, um"

455
 00:18:09,788 --> 00:18:12,515
 But, um, but, um, but, um...
 god help us all.
# '''
#import re
##print(re.findall('[b,B,o]ut, um', txt))
##print(re.search('but, um', txt).count())
#xx = "guru99,education is fun"
#r1 = re.findall(r"\w+", xx)
#print(r1)
#print((re.split(r'\s','we are splitting the words')))
#print((re.split(r's','split the words')))

#--------------------------------------------------------------------
#pandas Crosstab example
#https://pbpython.com/pandas-crosstab.html
import pandas as pd
import numpy as np
import seaborn as sns


headers_ =["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

## ? values ae set as NaN values
df_raw = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                     header=None, names=headers_, na_values="?" )


#define a list of models we want to review -- top 8
models = ["toyota","nissan","mazda", "honda", "mitsubishi", "subaru", "volkswagen", "volvo"]

#create a df copy of the data with only top 8 manufacturers
df = df_raw[df_raw['make'].isin(models)].copy()

#print(df.head(2))
#print(df.columns)

##crosstab easier for formatting and summarizing
#use crosstab o find how many body styles these car makers made in 1985
cross_pd = pd.crosstab(df.make, df.body_style)
#print(cross_pd) #df.make is the crosstab index and boystyle is the crosstabs columns

#same operation can be done using group by and unstack
groupby = df.groupby(['make', 'body_style'])['body_style'].count().unstack().fillna(0)
#print(group)

#same can be done pivot table
pivottable= df.pivot_table(index='make', columns='body_style', aggfunc={'body_style':len}, fill_value=0)
#print(pivottable)


##use margins to add aggregates like totals and subtotals
margin_crosstab = pd.crosstab(df.make, df.body_style, margins=True, margins_name='Total')
#print(margin_crosstab)

##to add more summarization like calculating ag=vg curb weigh of cars by body style
crosstab = pd.crosstab(df.make, df.body_style, values=df.curb_weight, aggfunc='mean').round(0)
print(crosstab)

#if we want to understand the percentage distributions of data
#normalize it
normalize = pd.crosstab(df.make, df.body_style, normalize=True) #percent of totals
normalizeOnColumns = pd.crosstab(df.make, df.body_style, normalize='columns') #find how body styles are distributed across makes
print(normalize)
print(normalizeOnColumns)

























