#%%
import pandas as  pd 
import numpy as np
#%%
df = pd.DataFrame({
            'name': ["John Smith", "Jane Doe", "Mary Johnson"],
            'treatment_a': [None, 16, 3], 
            'treatment_b': [2, 11, 1]})
df
#%% 
df_melt = pd.melt(df, id_vars='name')
df_melt
#%%
df
#%%
df_melt_pivot = pd.pivot_table(df_melt,
                               index='name',
                               columns='variable',
                               values='value')
                               
print(df_melt_pivot)
#%%
df_melt_pivot.reset_index()
#%%
#Exercise 8.2 (Import data) 
# Import Expression.txt. Save it as an object called medi.
medi = pd.read_csv('data/Expression.txt')
#%%
medi.info()
#%%
#%%
medi_index = medi.reset_index()
#%%

# Exercise 8.3 (Tidy data) Convert the data set to a tidy format.
medi_melt = pd.melt(medi_index, id_vars='index')
#%%
medi_melt
#%%
medi_melt = pd.melt(medi,
                                index='index',
                               columns='variable',
                               values='value')
medi_melt = medi_melt.sort_values(by=["index"])

#%%
# Exercise 8.4 (Calculate Statistics) 
# Calculate each of the following statistics for each of the unique 24 combinations of gene, treatment and time:
#average the mean of the value
#%%
# n the number of observations in each group

#%%
# SEM The standard error of the mean
#%%
# CIerror The 95% CI error defined by the t distribution
#lower95 The upper 95% CI limit
#upper95 The upper 95% CI limit

#%%
# Exercise 8.5 (Export data) 
# Now that you’ve processed your data, 
# refer to the following table and save a 
# file on your computer that contains the summary statistics.

