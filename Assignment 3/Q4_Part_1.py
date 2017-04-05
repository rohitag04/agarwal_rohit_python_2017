
# coding: utf-8

# ### Q4_Part 1
# - Things to do
#     - use movie_rewards data.
#     - Extract data from awards columns and split it into several columns.
#     - Create win and nominated columns and enter exact number of win and nominate count.

# In[2]:

import os
import pandas as pd
import numpy as np
# Offsetting the warning
import warnings
warnings.filterwarnings('ignore')


# In[3]:

# Get current working directory
currentWD = os.getcwd()

# Read CSV file
df = pd.read_csv(currentWD+"//"+"Assignment 3//movies_awards.csv", usecols=[15])


# In[4]:

# filtering the data frame for which awards is N/A
dfMovies = df.dropna()


# In[5]:

# spliiting data and creating columns 
dfMovies['Awards Wins'] = dfMovies['Awards'].str.extract('(\d+ win)', expand=True)
dfMovies['Awards Nominated'] = dfMovies['Awards'].str.extract('(\d+ nomination)', expand=True)
dfMovies['Primetime Emmys Wins'] = dfMovies['Awards'].str.extract('(Won \d+ Primetime Emmy)', expand=True)
dfMovies['Primetime Emmys Nominations'] = dfMovies['Awards'].str.extract('(Nominated for \d+ Primetime Emmy)', expand=True)
dfMovies['Oscar Nominations'] = dfMovies['Awards'].str.extract('(Nominated for \d+ Oscar)', expand=True)
dfMovies['Oscar Wins'] = dfMovies['Awards'].str.extract('(Won \d+ Oscar)', expand=True)
dfMovies['Golden Globe Nominations'] = dfMovies['Awards'].str.extract('(Nominated for \d+ Golden Globe)', expand=True)
dfMovies['Golden Globe Wins'] = dfMovies['Awards'].str.extract('(Won \d+ Golden Globe)', expand=True)
dfMovies['BAFTA Nominations'] = dfMovies['Awards'].str.extract('(Nominated for \d+ BAFTA)', expand=True)
dfMovies['BAFTA Wins'] = dfMovies['Awards'].str.extract('(Won \d+ BAFTA)', expand=True)


# In[6]:

#taking integers from the split strings
dfMovies['Awards Wins'] = dfMovies['Awards Wins'].str.extract('(\d+)')
dfMovies['Awards Nominated'] = dfMovies['Awards Nominated'].str.extract('(\d+)')
dfMovies['Oscar Nominations'] = dfMovies['Oscar Nominations'].str.extract('(\d+)')
dfMovies['Oscar Wins'] = dfMovies['Oscar Wins'].str.extract('(\d+)')
dfMovies['Primetime Emmys Nominations'] = dfMovies['Primetime Emmys Nominations'].str.extract('(\d+)')
dfMovies['Primetime Emmys Wins'] = dfMovies['Primetime Emmys Wins'].str.extract('(\d+)')
dfMovies['Golden Globe Nominations'] = dfMovies['Golden Globe Nominations'].str.extract('(\d+)')
dfMovies['Golden Globe Wins'] = dfMovies['Golden Globe Wins'].str.extract('(\d+)')
dfMovies['BAFTA Nominations'] = dfMovies['BAFTA Nominations'].str.extract('(\d+)')
dfMovies['BAFTA Wins'] = dfMovies['BAFTA Wins'].str.extract('(\d+)')


# In[7]:

#filling NaN with 0
dfMovies['Awards Wins'] = dfMovies['Awards Wins'].fillna(0)
dfMovies['Awards Nominated'] = dfMovies['Awards Nominated'].fillna(0)
dfMovies['Primetime Emmys Nominations'] = dfMovies['Primetime Emmys Nominations'].fillna(0)
dfMovies['Primetime Emmys Wins'] = dfMovies['Primetime Emmys Wins'].fillna(0)
dfMovies['Oscar Nominations'] = dfMovies['Oscar Nominations'].fillna(0)
dfMovies['Oscar Wins'] = dfMovies['Oscar Wins'].fillna(0)
dfMovies['Golden Globe Nominations'] = dfMovies['Golden Globe Nominations'].fillna(0)
dfMovies['Golden Globe Wins'] = dfMovies['Golden Globe Wins'].fillna(0)
dfMovies['BAFTA Nominations'] = dfMovies['BAFTA Nominations'].fillna(0)
dfMovies['BAFTA Wins'] = dfMovies['BAFTA Wins'].fillna(0)


# In[8]:

#converting the data-type from string to int
dfMovies['Awards Nominated'] = dfMovies['Awards Nominated'].astype(int)
dfMovies['Awards Wins'] = dfMovies['Awards Wins'].astype(int)
dfMovies['Oscar Nominations'] = dfMovies['Oscar Nominations'].astype(int)
dfMovies['Oscar Wins'] = dfMovies['Oscar Wins'].astype(int)
dfMovies['Primetime Emmys Nominations'] = dfMovies['Primetime Emmys Nominations'].astype(int)
dfMovies['Primetime Emmys Wins'] = dfMovies['Primetime Emmys Wins'].astype(int)
dfMovies['Golden Globe Nominations'] = dfMovies['Golden Globe Nominations'].astype(int)
dfMovies['Golden Globe Wins'] = dfMovies['Golden Globe Wins'].astype(int)
dfMovies['BAFTA Nominations'] = dfMovies['BAFTA Nominations'].astype(int)
dfMovies['BAFTA Wins'] = dfMovies['BAFTA Wins'].astype(int)


# In[9]:

#calculating total number of nominations and awards
dfMovies['Awards Nominated'] = dfMovies['Awards Nominated'] + dfMovies['Oscar Nominations'] + dfMovies['Primetime Emmys Nominations'] + dfMovies['Golden Globe Nominations'] + dfMovies['BAFTA Nominations']
dfMovies['Awards Wins'] = dfMovies['Awards Wins'] + dfMovies['Oscar Wins'] + dfMovies['Primetime Emmys Wins'] + dfMovies['Golden Globe Wins'] + dfMovies['BAFTA Wins']


# In[14]:

#columns to be printed on the console
columns = ['Awards', 'Awards Wins', 'Awards Nominated', 'Oscar Nominations', 'Oscar Wins', 'Primetime Emmys Nominations', 'Primetime Emmys Wins', 'Golden Globe Nominations', 'Golden Globe Wins', 'BAFTA Nominations', 'BAFTA Wins']


# In[13]:

print(dfMovies[columns].head().to_string(index=True))
#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = currentWD+'\\Assignment 3(Results)\\Q4_Part_1.csv'
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
dfMovies[columns].to_csv(resultsPath, index=False, encoding='utf-8')

