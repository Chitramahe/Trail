#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[2]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import OneHotEncoder
import pickle
import warnings
warnings.filterwarnings('ignore')


# # Importing Raw Data

# In[3]:


data_cab = pd.read_csv('C://Users//Chitra//Desktop//Yourcabs_1.csv')
data_cab


# # Exploratory Data Analysis

# In[4]:


## No. of Rows and Columns
data_cab.shape


# In[5]:


## Analysis the basic information of Raw data
data_cab.info()


# In[7]:


## Analysing the statistical information of Raw data
data_cab.describe()


# In[8]:


## Finding out the null values
data_cab.isnull().sum()


# In[9]:


## Removing the columns which are not relevant for our analysis
data_cab=data_cab.drop(['package_id','to_area_id','from_city_id','to_city_id','from_long','to_lat','to_long'],axis=1)


# In[10]:


## No. of Rows and Columns after dropping unwanted columns
data_cab.shape


# In[11]:


## Checking remaining columns for null values
data_cab.info()


# In[12]:


## Replacing the null values with mode

columns=['from_area_id','from_lat']
for col in columns:
    value=data_cab[col].mode().iloc[0]
    data_cab[col].fillna(value,inplace=True)


# In[13]:


## Checking for null values once again.
data_cab.info() ## Now no null values will be present


# In[14]:


## Splitting the data in to training and testing

x = data_cab.drop(['Car_Cancellation'],axis=1)
y = data_cab['Car_Cancellation']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=100)


# In[15]:


data_cab.columns


# In[16]:


features='travel_type_id','from_area_id','from_date','online_booking','mobile_site_booking','booking_created','from_lat'
target='Car_Cancellation'

