
# coding: utf-8

# ### Q1_Part 1
# - Things to do
#     - use vehicle_collision data.
#     - For each month in 2016 find % of collision in Manhattan with total accidents in NYC.
#     - Generate CSV with 4 columns(Month, Manhattan, NYC, %)

# In[1]:

import os
import pandas as pd


# In[3]:

# Getting current working directory
currentDirect = os.getcwd()

# Reading vehicle_collison file store in Assignment 3 folder in cuurentDirect using pandas read_csv & converting Date Object
# to DATETIME Format

df = pd.read_csv(currentDirect+"//"+"Assignment 3"+"//"+"vehicle_collisions.csv" , parse_dates=['DATE'], usecols=[0,1,3])


# In[4]:

# Now task is to filter all date for the year 2016
dfYear = df[df.DATE.dt.year == 2016]


# In[5]:

# Offsetting the warning
pd.options.mode.chained_assignment = None

# Now task is to Group The Dataframe on basis of month
dfYear['Month'] = dfYear['DATE'].dt.strftime('%b')


# In[6]:

# Now will group our Data by month & find the COunt
NYC = dfYear['UNIQUE KEY'].groupby(dfYear['Month']).count()

# Sorting month according to month name
NYC.index = pd.CategoricalIndex(NYC.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
NYC = NYC.sort_index()


# In[7]:

# Now will group our Data by month where BOROUGH = MANHATTAN & find the COunt
Manhattan = dfYear['UNIQUE KEY'][dfYear['BOROUGH'] == "MANHATTAN"].groupby(dfYear['Month']).count()

# Sorting month according to month name
Manhattan.index = pd.CategoricalIndex(Manhattan.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
Manhattan = Manhattan.sort_index()


# In[8]:

# Create new Data frame 
Columns = ["Month", "Manhattan", "NYC", "Percentage"]
dataFrame = pd.DataFrame({'Month' : NYC.index, 'Manhattan' : Manhattan, 'NYC' : NYC, 'Percentage' : Manhattan / NYC})
print(dataFrame[Columns].head().to_string(index=True))


# In[9]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = currentDirect+'\\Assignment 3(Results)\\Q1_Part_1.csv'
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
dataFrame[Columns].to_csv(resultsPath, index=False, encoding='utf-8')

