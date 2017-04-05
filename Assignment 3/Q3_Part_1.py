
# coding: utf-8

# ### Q3_Part 1
# - Things to do
#     - use cricket_matches data.
#     - Calculate average score of each team where host team == winning team
#     - Generate CSV with 4 columns(Month, Manhattan, NYC, %)

# In[2]:

import os
import pandas as pd


# In[3]:

# Getting current working directory
currentDirect = os.getcwd()

# Reading vehicle_collison file store in Assignment 3 folder in cuurentDirect using pandas read_csv & converting Date Object
# to DATETIME Format

df = pd.read_csv(currentDirect+"//"+"Assignment 3"+"//"+"cricket_matches.csv" , usecols=[6,7,8,12,13,17,18])


# In[5]:

# Sorting home by Ascending 
sortedDF = df.sort_values(['home'], ascending=True)

# Checking if home == winner == inning1
sortInninig1 = sortedDF[(sortedDF['home'] == sortedDF['winner']) & (sortedDF['winner'] == sortedDF['innings1'])]

# Checking if home == winner == inning2
sortInninig2 = sortedDF[(sortedDF['home'] == sortedDF['winner']) & (sortedDF['winner'] == sortedDF['innings2'])]

# Creating Data Frames for both inning
df1 = pd.DataFrame({'home': sortInninig1['home'], 'Runs': sortInninig1['innings1_runs']})
df2 = pd.DataFrame({'home': sortInninig2['home'], 'Runs': sortInninig2['innings2_runs']})


# In[6]:

# Concating both DF
runs = df1.append(df2, ignore_index=True)


# In[7]:

# Finding sum of all runs
runsGroup = runs['Runs'].groupby(runs['home']).sum()

# Finding count of Home
homeGroup = runs['Runs'].groupby(runs['home']).count()


# In[8]:

# Creating Final Dataframe
columns = ['Home', 'Score']
finalScore = pd.DataFrame({'Home' : homeGroup.index, 'Score' : runsGroup / homeGroup})

print(finalScore[columns].head())


# In[9]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = currentDirect+'\\Assignment 3(Results)\\Q3_Part_1.csv'
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
finalScore[columns].to_csv(resultsPath, index=False, encoding='utf-8')

