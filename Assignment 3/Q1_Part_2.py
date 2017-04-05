
# coding: utf-8

# ### Q1_Part 2
# - Things to do
#     - use vehicle_collision data.
#     - For Each Borough find out distribution of each collision scale. (One Car Involved, Two Car Involved, Three or more)
#     - Generate CSV with 5 columns(Borough, One_vehicle_involved, Two_vehicle_involved, Three_vehicle_involved, More_vehicle_involved)

# In[1]:

import os
import pandas as pd


# In[2]:

# get current working directory
currentDirec = os.getcwd()

# Reading csv file in order to get dataframe.
df = pd.read_csv(currentDirec+"//"+"Assignment 3"+"//"+"vehicle_collisions.csv", usecols=[0,3,19,20,21,22,23])


# In[3]:

# Creating unique key & borough as DF
df_location = df[['UNIQUE KEY','BOROUGH']]

# Taking all types of Vehicle
df_vehicle = df[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]

#Removing NAN values
df_type = df_vehicle.notnull()

# Assigning 0 & 1 to all nan values
df_type = df_type.applymap(lambda x:1 if x else 0)

# Concating both DF
df_type = pd.concat([df_location, df_type], axis=1)


# In[4]:

# Taking out the sum of all Borough group by
result = df_type.groupby(df_type['BOROUGH']).sum()


# In[5]:

# Creating Final data frame
columns = ['Borough', 'One_V_I', 'Two_V_I', 'Three_V_I', 'more_v_I']
finalResult = pd.DataFrame({'Borough' : result.index, 'One_V_I' : result['VEHICLE 1 TYPE']-result['VEHICLE 2 TYPE'], 
                           'Two_V_I' : result['VEHICLE 2 TYPE']-result['VEHICLE 3 TYPE'], 'Three_V_I' : result['VEHICLE 3 TYPE']-result['VEHICLE 4 TYPE'],
                           'more_v_I' : result['VEHICLE 4 TYPE'] })

print(finalResult[columns].head())


# In[95]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = currentDirec+'\\Assignment 3(Results)\\Q1_Part_2.csv'
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
finalResult[columns].to_csv(resultsPath, index=False, encoding='utf-8')

