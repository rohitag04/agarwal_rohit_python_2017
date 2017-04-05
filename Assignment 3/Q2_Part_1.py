
# coding: utf-8

# ## Things to do
# - Use Employee Compensation dataset.
#     - Find out highest paid department in each organization group by calculating mean of total compensation for each department.
#     - Output should be from lowest to highest
#     - [Coomunity Health, Public Health, Total Compensation]

# In[1]:

import os
import pandas as pd


# In[40]:

# get current working directory
currentWD = os.getcwd()

# read csv and cosidering only those columns which are useful
df = pd.read_csv(currentWD+"//"+"Assignment 3//employee_compensation.csv", usecols=[3,5,21])
df.head()


# In[130]:

# Grouping by Employee Identifier and Job Family and finding mean
compen = df.groupby(['Organization Group','Department']).mean()

# reseeting the index
compen = compen.reset_index()


# In[145]:

compenSort = compen.sort_values(['Organization Group','Total Compensation'],ascending = [True, False])
print(compenSort.head())


# In[143]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = currentWD+'\\Assignment 3(Results)\\Q2_Part_1.csv'
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
compenSort.to_csv(resultsPath, index=False, encoding='utf-8')

