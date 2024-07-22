#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from math import ceil
plt.style.use('_mpl-gallery')


# In[4]:


# importing data
data = pd.read_csv('/Users/sarthakchawla/Downloads/EnglandWeather.csv')
data


# In[5]:


df = pd.DataFrame(data)
df_rows_count, df_columns_count = df.shape
print(f'number of samples: {df_rows_count}')
print(f'number of columns: {df_columns_count}')
df.head(7)


# In[6]:


# data profilling
def check_df(df: object, head: object = 5) -> object:
    print("\nShape")
    print(df.shape)
    print("\nTypes")
    print(df.dtypes)
    print("\nNANs")
    print(df.isnull().sum())
    print("\nInfo")
    print(df.info())
check_df(df)


# In[7]:


print('Number of duplicated rows: ' , len(df[df.duplicated()]))
df[df.duplicated()]


# In[8]:


# droping dublicated rows
df = df.drop_duplicates()
df


# In[9]:


plt.figure(figsize=(22,4))
sns.heatmap((df.isna().sum()).to_frame(name='').T,cmap='YlOrBr', annot=True,
             fmt='0.0f').set_title('Count of Missing Values', fontsize=18)
plt.show()


# In[10]:



import missingno as msno
msno.bar(df, color='#f4a261')
plt.show()


# In[11]:



# finding unique data
df.apply(lambda x: len(x.unique()))


# In[12]:



unique = df.nunique().sort_values()
unique_values = df.apply(lambda x: x.unique())
pd.DataFrame({'Number of Unique Values': unique, 'Unique Values': unique_values})


# In[19]:


df[df['Temperature (C)'] >= 0]['Precip Type'].value_counts()


# In[20]:


df2 = df.copy()
df2.fillna('rain', inplace=True)


# In[21]:


df2


# In[22]:


# verifing
df2.isna().sum()


# In[23]:


# converting formatted date type to datetime
df2[['date', 'time']] = df2['Formatted Date'].str.split(' ', n=1, expand=True)
df3 = df2.drop('Formatted Date', axis=1)
df3


# In[24]:


df3["date"] = pd.to_datetime(df3["date"], format='%Y-%m-%d')
df3['year'] = df3['date'].dt.year
df3["month"] = df3["date"].dt.month
df3['day'] = df3['date'].dt.day
df3['hour'] = df3['date'].dt.hour
df3.head()


# In[25]:


# standardize
df3['Humidity'] = df3['Humidity']*100 # convert Humidity to percent
df3 = df3.sort_values('date') # sort values by Formatted Date
df3 = df3.reset_index(drop=True)
df3


# In[26]:



def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'
df3['season'] = df3['month'].apply(get_season)


# In[27]:


def split_time(hour):
    if 0 <= hour <= 11:
        return "Morning"
    elif 12 <= hour <= 24:
        return "Evening"
    else:
        return "nan"
df3['M/E'] = df3['hour'].apply(split_time)
df3


# In[28]:


df3.sort_values(by=['year', 'month', 'day', 'hour'], inplace=True)
df3


# In[29]:


cols = df3.columns.to_list()
cols = cols[-2:] + cols[:-2]
df3 = df3[cols]
df3.dtypes


# In[30]:


df3.info()


# In[31]:



df4=pd.DataFrame(df3,columns=["Summary","Precip Type","season"])
df4


# In[32]:


df4.describe()


# In[33]:


from IPython.core.display import HTML
def multi_table(table_list):
    return HTML(
        '<table><tr style="background-color:white;">' + 
        ''.join(['<td>' + table._repr_html_() + '</td>' for table in table_list]) +
        '</tr></table>')


# In[34]:


print("Percentages of each unique value of categorical features:")
nunique = {var: pd.DataFrame((df3[var].value_counts()/len(df3[var])*100).map('{:.3f}%'.format)) 
              for var in {'season', 'M/E', 'Summary', 'Precip Type'}}
multi_table([nunique['season'],nunique['M/E'],nunique['Summary'],nunique['Precip Type']])


# In[ ]:




