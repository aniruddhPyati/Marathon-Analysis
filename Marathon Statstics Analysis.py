#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas ')


# In[2]:


import pandas as pd


# In[3]:


import seaborn as sns


# In[4]:


data_df=pd.read_csv('TWO_CENTURIES_OF_UM_RACES.csv')


# In[5]:


data_df


# In[6]:


data_df.shape


# In[8]:


data_df.dtypes


# In[13]:


data_df[data_df['Event distance/length']=='50mi'].head(5)


# In[14]:


data_df[data_df['Event distance/length'].isin(['50km','50mi'])]


# In[17]:


data_df[ (data_df['Event distance/length'].isin(['50km','50mi'])) & (data_df['Year of event']==2020) ]


# In[19]:


data_df[data_df['Event name']=='Everglades 50 Mile Ultra Run (USA)']


# In[23]:


data_df[data_df['Event name']=='Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)


# In[30]:


data_df[data_df['Event name']=='USA']


# In[31]:


data_df[data_df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)=='USA']


# In[33]:


data_df.loc[data_df['Athlete country']=='USA','Event name']


# In[36]:


data2_df=data_df[ (data_df['Event distance/length'].isin(['50km','50mi'])) & (data_df['Year of event']==2020) &(data_df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)=='USA') ]  


# In[37]:


data2_df.head(10)


# In[38]:


data2_df['Event name']


# In[39]:


data2_df['Event name'].str.split('(').str.get(0)


# In[40]:


data2_df['Event name']=data2_df['Event name'].str.split('(').str.get(0)


# In[41]:


data2_df.head(10)


# In[45]:


data2_df['athlete_age']= 2020- data2_df['Athlete year of birth']


# In[46]:


data2_df.head(10)


# In[48]:


data2_df['Athlete performance']=data2_df['Athlete performance'].str.split(' ').str.get(0)


# In[49]:


data2_df.head(5)


# In[51]:


data2_df=data2_df.drop(['Athlete club','Athlete country','Athlete year of birth','Athlete age category'],axis=1)


# In[53]:


data2_df


# In[54]:


data2_df.isna().sum() 


# In[55]:


data2_df[data2_df['athlete_age'].isna()==1]


# In[57]:


data2_df=data2_df.dropna()


# In[60]:


data2_df


# In[59]:


data2_df[data2_df.duplicated()==True]


# In[61]:


data2_df.reset_index(drop=True)


# In[62]:


data2_df.dtypes


# In[66]:


data2_df['athlete_age']= data2_df['athlete_age'].astype(int)


# In[67]:


data2_df.dtypes


# In[68]:


data2_df['Athlete average speed']=data2_df['Athlete average speed'].astype(float)


# In[69]:


data2_df.dtypes


# In[70]:


data2_df.head(5)


# In[81]:


data2_df=data2_df.rename(columns={
    'Year of event':'Year',
    'Event dates':'race_date',
    'Event name':'race_name',
    'Event distance/length':'race_length',
    'Athlete performance':'athlete_performance',
    'Athlete gender':'gender',
    'Athlete average speed':'Athlete_average_speed',
    'Athlete ID':'athlete_id',
    'Event number of finishers':'number_of_finishers'
})


# In[82]:


data2_df.head(2)


# In[86]:


data2_df[data2_df['race_name']=='Everglades 50 Mile Ultra Run ']


# In[88]:


data2_df[data2_df['athlete_id']==46432]


# In[91]:


data2_df.head(2)


# In[97]:


## Toughest races of all time 
data2_df.loc[data2_df['number_of_finishers']==2,'race_name']


# ## VISUALIZATION

# In[101]:


## Number of 50km and 50mi races
sns.histplot(x='race_length',data=data2_df)


# In[103]:


sns.histplot(data2_df,x='race_length',hue='Gender')


# In[104]:


sns.displot(data2_df[data2_df['race_length']=='50mi']['Athlete_average_speed'])


# In[105]:


sns.displot(data2_df[data2_df['race_length']=='50km']['Athlete_average_speed'])


# In[112]:


sns.violinplot(data=data2_df,x='race_length',y='Athlete_average_speed',hue='Gender',split=True,inner='quart')


# In[115]:


sns.lmplot(data=data2_df,x='athlete_age',y='Athlete_average_speed',hue='athlete_age')


# ####  Speeds for the 50km and 50mi races gender wise
# 

# In[117]:


data2_df.groupby(['race_length','Gender'])['Athlete_average_speed'].mean()


# #### Number of finishers in every race

# In[124]:


data2_df.groupby(['race_name'])['number_of_finishers'].sum()


# ### Race speeds and participation affected by season

# In[125]:


data2_df['month']=data2_df['race_date'].str.split('.').str.get(1).astype(int)


# In[126]:


data2_df.head(3)


# In[128]:


data2_df['race_season']=data2_df['month'].apply(lambda x: 'Winter' if x>11 else 'Summer' if x>5 else 'Spring' )


# In[132]:


data2_df.tail(3)


# In[135]:


data2_df.groupby(['race_season'])['Athlete_average_speed'].agg(['mean','count'])


# In[136]:


## For 50 km races only
data2_df.query('race_length=="50mi"').groupby(['race_season'])['Athlete_average_speed'].agg(['mean','count'])


# ### Race speeds and participation affected by season gender wise

# In[140]:


data2_df.groupby(['race_season','Gender'])['Athlete_average_speed'].agg(['mean','count'])


# In[ ]:




