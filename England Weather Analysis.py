#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from math import ceil
plt.style.use('_mpl-gallery')


# In[6]:


# importing data
data = pd.read_csv('/Users/sarthakchawla/Downloads/EnglandWeather.csv')
data


# In[7]:


df = pd.DataFrame(data)
df_rows_count, df_columns_count = df.shape
print(f'number of samples: {df_rows_count}')
print(f'number of columns: {df_columns_count}')
df.head(7)


# In[8]:


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


# In[9]:


print('Number of duplicated rows: ' , len(df[df.duplicated()]))
df[df.duplicated()]


# In[10]:


# droping dublicated rows
df = df.drop_duplicates()
df


# In[11]:


plt.figure(figsize=(22,4))
sns.heatmap((df.isna().sum()).to_frame(name='').T,cmap='YlOrBr', annot=True,
             fmt='0.0f').set_title('Count of Missing Values', fontsize=18)
plt.show()


# In[12]:



import missingno as msno
msno.bar(df, color='#f4a261')
plt.show()


# In[13]:



# finding unique data
df.apply(lambda x: len(x.unique()))


# In[14]:



unique = df.nunique().sort_values()
unique_values = df.apply(lambda x: x.unique())
pd.DataFrame({'Number of Unique Values': unique, 'Unique Values': unique_values})


# In[ ]:




