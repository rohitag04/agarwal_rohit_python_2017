
# coding: utf-8

# ### Q2_Part 2
# - Things to do
#     - use employee_compensation data.
#     - For each job family calculate % of Total benefits, compensation, % total benefit

# In[2]:

import os
import pandas as pd


# In[3]:

# get current working directory
currentWD = os.getcwd()

# Read CSV File
df = pd.read_csv(currentWD+"//"+"Assignment 3/employee_compensation.csv", usecols=[0,1,9,12,13,14,20,21])


# In[4]:

# Filtering on the basis of Calendar
dfYear = df[(df['Year Type']=='Calendar')]


# In[5]:

# Grouping by Employee Identifier and Job Family and finding mean
compen = pd.DataFrame(dfYear.groupby(['Employee Identifier','Job Family']).mean())


# In[11]:

# find overtime salaray
overtime = compen[(compen['Overtime'] > (.05 * compen['Salaries']))]


# In[12]:

# Grouping by JOB FAMILY And Finiding Mean
top_family = overtime.groupby([overtime.index.get_level_values(1)]).mean()

top_family = top_family[['Total Benefits','Total Compensation']]

# Calculating % Total
top_family['Percent_Total_Benefit'] = 100 * (top_family['Total Benefits'] / top_family['Total Compensation'])

# Sorting Values
top_family = top_family.sort_values(['Percent_Total_Benefit'], ascending=[False])

#creating dataframe
columns = ['Job Family', 'Total Benefits', 'Total Compensation', 'Percent_Total_Benefit']
result = pd.DataFrame({'Job Family' : top_family.index, 'Total Benefits' : top_family['Total Benefits'],
                      'Total Compensation' : top_family['Total Compensation'], 'Percent_Total_Benefit' : top_family['Percent_Total_Benefit']})

# Printing to show 5 records
print(result[columns].head().to_string(index=True))


# In[32]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = currentWD+'\\Assignment 3(Results)\\Q2_Part_2.csv'
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
result[columns].to_csv(resultsPath, index=False, encoding='utf-8')

