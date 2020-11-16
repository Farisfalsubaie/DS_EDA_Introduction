#%%
#Chapter 7 Case-study: Diamonds
import math 
import pandas as pd 
import numpy as np 

import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
#%%
#Import the data set and assign it to the variable mtcars.
diamonds = pd.read_csv('data/diamonds.csv')
diamonds

#%%
#Exercise 7.2 (Examine structure) 
# Can you examine the structure of the DataFrame?
# What type of data is contained in each column?
diamonds.info()

#%%
#Exercise 7.3 (Counting individual groups) 
# How many diamonds with a clarity of category “IF” are present in the data-set?
# 
diamonds[diamonds.clarity =="IF"]
diamonds[diamonds.clarity =="IF"].count()
#%%What fraction of the total do they represent?
len(diamonds[(diamonds.clarity == 'IF')])/len(diamonds)
#%%
diamonds.clarity.value.count()

#%%
#Exercise 7.5 (Find specific diamonds prices) 
#  What is the cheapest diamond price overall?
min(diamonds.price) 
#%%  What is the range of diamond prices? 
len(diamonds.price)
print('Range for prices','(',diamonds['price'].min(),'-', diamonds['price'].max(),')')
#%%

def getRange (l):
    low = min(l)
    high = max(l)
    return low, high

getRange(diamonds.price)
low, high = getRange(diamonds.price)
#%%
getRange(diamonds.price)


#%%  What is the average diamond price in each category of cut and color?
diamonds.groupby(['cut','color'])['price'].mean()

#np.mean(diamonds.cut)

#%%
#Exercise 7.6 (Basic plotting)
#  Make a scatter plot that shows the diamond price described by carat.

plt.plot( 'carat','price',  data=diamonds)
plt.show()


#%%
#Exercise 7.7 (Applying transformations) 
# Apply a log10 transformation to both the price and carat and store these 
# as new columns in the DataFrame: price_log10 and carat_log10.
diamonds['carat_log10'] = math.log10(diamonds['carat'])

diamonds['price_log10'] = math.log10(diamonds['price'])



#%%
#Exercise 7.8 (Basic plotting) 
# Redraw the scatterplot using the transformed values.




#%%
#Exercise 7.9 (Viewing models) 
# Define a linear model that describes the relatioship shown in the plot.



