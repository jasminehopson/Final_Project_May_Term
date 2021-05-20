#!/usr/bin/env python
# coding: utf-8

# In[64]:


from math import *
from random import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Computing the Mean and Standard Error

# In[65]:


df = pd.read_csv(r'/Users/mina/Downloads/data3.csv')
df.head()


# In[66]:


average = df.mean(axis = 0, skipna = True)
print("mean = ", average) #uses data frame using panda package


# In[67]:


se = df.sem(axis = 0)
sd = df.std(axis = 0)
print("Standard Deviation = ", sd)
print("standard error = ", se)


# Making the Graph of CDF

# In[68]:


df.hist(cumulative=True)
plt.xlabel('Measurement Number')
plt.ylabel('Measurement')
plt.title('CDF')
plt.grid()


# In[74]:


#second half getting data
dataframe = [0] * (10)
dataframe[0] = pd.read_csv(r'/Users/mina/Downloads/1000.csv')
dataframe[1] = pd.read_csv(r'/Users/mina/Downloads/2000.csv')
dataframe[2] = pd.read_csv(r'/Users/mina/Downloads/3000.csv')
dataframe[3] = pd.read_csv(r'/Users/mina/Downloads/4000.csv')
dataframe[4] = pd.read_csv(r'/Users/mina/Downloads/5000.csv')
dataframe[5] = pd.read_csv(r'/Users/mina/Downloads/6000.csv')
dataframe[6] = pd.read_csv(r'/Users/mina/Downloads/7000.csv')
dataframe[7] = pd.read_csv(r'/Users/mina/Downloads/8000.csv')
dataframe[8] = pd.read_csv(r'/Users/mina/Downloads/9000.csv')
dataframe[9] = pd.read_csv(r'/Users/mina/Downloads/10000.csv')


# In[75]:


#Creating the x axis
x = [0] * (10)
x[0] = 10
i = 1
while(i<10):
    x[i] = x[i-1] + 10
    i += 1


# In[76]:


#Creating the y axis
SEList = [0] * (10)
SEList[0] = dataframe[0].sem(axis = 0)
SEList[1] = dataframe[1].sem(axis = 0)
SEList[2] = dataframe[2].sem(axis = 0)
SEList[3] = dataframe[3].sem(axis = 0)
SEList[4] = dataframe[4].sem(axis = 0)
SEList[5] = dataframe[5].sem(axis = 0)
SEList[6] = dataframe[6].sem(axis = 0)
SEList[7] = dataframe[7].sem(axis = 0)
SEList[8] = dataframe[8].sem(axis = 0)
SEList[9] = dataframe[9].sem(axis = 0)


# In[77]:


#Making the graph
plt.plot(x, SEList, marker="o", linestyle="None")
plt.grid()
plt.xlabel('Measurement Number')
plt.ylabel('Measurement')
plt.title('Scatterplot for Standard Error')


# In[ ]:




