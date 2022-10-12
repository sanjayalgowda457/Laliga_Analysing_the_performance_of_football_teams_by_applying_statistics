#!/usr/bin/env python
# coding: utf-8

# # Project-1 | Statistical Learning
# You are required to do the following:
# 
# Read the data set and replace dashes with 0 to make sure you can perform arithmetic operations on the data. (5 points) Print all the teams which have started playing between 1930-1980. (5 points) Print the list of teams which came Top 5 in terms of points (5 points) Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences. Using the same function, find the team which has maximum and minimum goal difference.
# (5 points) Goal_diff_count = GoalsFor - GoalsAgainst 
# Create a new column with name “Winning Percent” and append it to the data set (5 points) 
# Percentage of Winning = (GamesWon / GamesPlayed)*100
# If there are any numerical error, replace it with 0% Print the top 5 teams which has the highest Winning percentage Group teams based on their “Best position” and print the sum of their points for all positions (5 points) 
#  Eg: Best Position Points
#    1                              25000
#    2                              7000  
# 
# Context: La Liga is the men's top professional football division of the Spanish football league system. The dataset contains information on all the teams that have participated in all the past tournaments. It has data about how many goals each team scored, conceded, how many times they came within the first 6 positions, how many seasons they have qualified, their best position in the past, etc. Data Description: Laliga.csv - The data set contains information on all the teams so far participated in all the past tournaments

# In[1]:


import numpy as np
import pandas as pd


# # 1. Read the data set
# 

# In[17]:


df_Laliga = pd.read_csv('C:/Users/CSC/Downloads/Laliga_csv.csv')


# In[18]:


df_Laliga.head()


# In[19]:


df_Laliga.tail(5)


# In[20]:


#Print a concise summary of a DataFrame.
df_Laliga.info()


# In[21]:


df_Laliga.shape


# # Replace dashes with 0

# In[22]:


# Using replace() - Replace values given in `to_replace` with `value`.
df_Laliga.replace('-',0,inplace=True)


# # Airthematic operation - Addition/Substraction/Multiplication/Division

# In[23]:


# Checking operations.
# Convert the datatype into int for performing the operations.


# Considering the champions and runnerup in (Deportivo La Coruna) team.
#Addition
df_Laliga.iloc[:,10].astype(int) + df_Laliga.iloc[:,11].astype(int)

#Substraction
#df_Laliga.iloc[:,10].astype(int) - df_Laliga.iloc[:,11].astype(int)

#Multiplication
#df_Laliga.iloc[:,10].astype(int) * df_Laliga.iloc[:,11].astype(int)

#Division
#x = df_Laliga.iloc[:,10].astype(int)/df_Laliga.iloc[:,11].astype(int)
#x.replace(np.inf, np.nan, inplace = True)
#x.fillna(0,inplace = True)
#x  


# # 2. Below teams started playing between 1930-1980.

# In[ ]:





# In[24]:


#Using Series.str and slice the first 4 characters, then cast to int:Then filter with Series.between and boolean indexing:
df_DebutYear = df_Laliga[df_Laliga['Debut'].astype(str).str[:4].astype(int).between(1930, 1980)]


# df_DebutYear[['Team','Debut']].count()   #37rows
df_DebutYear[['Team','Debut']]


# # 3. Print the list of teams which came Top 5 in terms of points

# In[25]:


# For using sort_values() function changing the datatype from str to int.
df_Laliga['Points'] = df_Laliga['Points'].astype(int)


# In[26]:


# Giving "ascending = False" for getting the largest values on the top or arranging it in the descending order. Using head()
# for picking top records.
df_Laliga[['Points','Team']].sort_values(by = 'Points',ascending = False).head(5)


# # 4. Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences.
# Using the same function, find the team which has maximum and minimum goal difference. (5 points) Goal_diff_count = GoalsFor - GoalsAgainst

# In[27]:


def Goal_diff_count():   
     df_Laliga['Goal_diff_count'] = df_Laliga['GoalsFor'].astype(int)-df_Laliga['GoalsAgainst'].astype(int)
     # if require to get the absolute value below line can be used
     # df_Laliga['Goal_diff_count'] = df_Laliga['Goal_diff_count'].abs()
     return df_Laliga[['Team','Goal_diff_count']].sort_values(by = 'Goal_diff_count',ascending=False)
    
Goal_diff_count()


# In[28]:


print("The team which has maximum goal difference is :")
Goal_diff_count().head(1)


# In[29]:


print("The team which has minimum goal difference is :")
Goal_diff_count().tail(1)


# # 5.Create a new column with name “Winning Percent” and append it to the data set (5 points) Percentage of Winning = (GamesWon / GamesPlayed)*100 If there are any numerical error, replace it with 0%
# Print the top 5 teams which has the highest Winning percentage

# In[36]:


#Percentage of Winning = (GamesWon / GamesPlayed)*100 
df_Laliga['Winning Percent'] = (df_Laliga['GamesWon'].astype(int)/df_Laliga['GamesPlayed'].astype(int)) *100


# In[37]:


df_Laliga['Winning Percent'].fillna(0,inplace = True)


# In[38]:


#Check
df_Laliga[['Team','Winning Percent']].head(20)


# # 6. Group teams based on their “Best position” and print the sum of their points for all positions (5 points)
# Eg: BestPosition Points 1 25000 2 7000

# In[33]:


# Storing in the object for using sum().
grouped_BestPosition = df_Laliga[['Team','Points','BestPosition']].groupby('BestPosition')
grouped_BestPosition


# In[34]:


#Compute sum of group values
grouped_BestPosition.sum()


# # Project Completed!!!
# Completed by: Sanjay A L Email: sanjay1999al@gmail.com

# In[ ]:




