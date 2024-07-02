#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import numpy as np  # Numpy Library
import pandas as pd # Pandas Library
import requests   # Checking Whether Permission Has been Granted or not
from bs4 import BeautifulSoup  # Webscraping package


# In[4]:


url = 'https://www.imdb.com/list/ls000040646/'
response = requests.get(url)
response


# In[32]:


soup = BeautifulSoup(response.content,'html.parser')


# In[ ]:


movie_data = soup.findAll('div',attrs={'class':'lister-item-content'})
movie_data


# In[158]:


#Initializing empty list
Movie_name = []
Year = []
Time = []
Genre = []
Rating = []
Metascore = []
Votes = []

for data in movie_data:
    name = data.h3.a.text
    Movie_name.append(name)
    
    
    Year1 = data.h3.find('span',attrs = {'class':'lister-item-year text-muted unbold'}).text.replace('(','').replace(')','')
    Year.append(Year1)
    
    
    Time1 = data.p.find('span',attrs = {'class':'runtime'}).text.replace(' min','')
    Time.append(Time1)
    
    Genre1 = data.p.find('span',attrs = {'class':'genre'}).text.replace('\n','').replace('  ','')
    Genre.append(Genre1)
    
    Rating1 = data.find('span',attrs = {'class':'ipl-rating-star__rating'}).text
    Rating.append(Rating1)
    
    Metascore1 = data.find('div',attrs = {'class':'inline-block ratings-metascore'}).text.replace('\n','').replace('  ','').replace('Metascore','') if (data.find('div',attrs = {'class':'inline-block ratings-metascore'})) else '####'
    Metascore.append(Metascore1)
    
    
    value = data.find_all('span',attrs = {'name':'nv'})
    
    Votes1= value[0].text.replace(',','')
    Votes.append(Votes1)
    
    


# In[159]:


df = pd.DataFrame({'Movie_name':Movie_name,'Year':Year,'Time':Time,'Genre':Genre,'Rating':Rating,'Metascore':Metascore,'Votes':Votes})


# In[160]:


df


# In[157]:


# Extracting the data into excel
df.to_excel("c:\\Users\\Chitra\\Desktop\\IMDB_Jackie Chan.xlsx")

