#!/usr/bin/env python
# coding: utf-8

# # Vikram Markali

# In[2]:


#import Libraries....
import pandas as pd


# In[5]:


#reading dataset....
data = pd.read_csv('D:/DYP/5th Sem/LAB/ML/Heart.csv')


# In[7]:


#displaying dataset using head()
data.head()


# In[14]:


#displaying dataset using tail()
data.tail()


# In[16]:


#describe the dataset...
data.describe()


# In[9]:


#finding shape of dataset...
data.shape


# In[10]:


#checking datatypes of dataset...
data.dtypes


# In[11]:


#finding mean of an attribute from dataset...
data['Age'].mean()


# In[13]:


#checking out missing values dataset...
data.isnull().count()


# In[18]:


#finding the unique values...
data['ChestPain'].unique()


# In[19]:


#finding the count of unique values...
data['ChestPain'].nunique()


# ### Coverting string values into numeric

# In[20]:


#before converting....
data['AHD']


# In[22]:


#coverting string into numeric....
data['AHD'] = data['AHD'].map({'Yes':1,'No':0})


# In[23]:


#after coverting....
data['AHD']


# In[24]:


data['ChestPain'] = data['ChestPain'].map({'typical':1,'asymptomatic':2,'nonanginal':3,'nontypical':4})


# In[25]:


data['ChestPain']


# In[26]:


data.head()


# In[27]:


#displaying columns of dataset...
data.columns


# In[28]:


#renaming the attributes...
data.rename(columns={'MaxHR':'MaxHRNew'})


# In[29]:


#displaying max value....
data['Age'].max()


# In[30]:


#displaying min value....
data['Age'].min()


# In[ ]:




