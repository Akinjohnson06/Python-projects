#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# first lets read january sales data
jan = r"C:\Users\DELL\Desktop\SalesAnalysis\Sales_Data\Sales_January_2019.csv"
df = pd.read_csv(jan)
df.head()


# In[3]:


# 12 months of sales data
# showing the whole sales data for the 12 months

all_data = r"C:\Users\DELL\Desktop\SalesAnalysis\Output\all_data.csv"
all_data = pd.read_csv(all_data)
all_data


# In[4]:


# Add month column, so its easier for us to read the months
all_data['Month'] = all_data['Order Date'].str[0:2]
# converting the month column to an integer
all_data['Month'] = all_data['Month'].astype('int')
all_data.head()


# In[5]:


# check the data types for each columns
all_data.dtypes


# ### Question 1: What was the best month for sales? How much was earned that month?

# In[6]:


all_data


# In[7]:


# looking at the data sets, we need a sales column to get our best month for sales
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data


# In[8]:


# now that we have our sales column, lets find the best month for sales
total_sales_per_month = all_data.groupby('Month')['Sales'].sum()
total_sales_per_month #this result gives you a Series


# In[9]:


total_sales_per_month1 = all_data.groupby('Month', as_index=False)['Sales'].sum()
total_sales_per_month1 #this results gives a dataframe


# In[10]:


# this answers the second part of the question
all_data.groupby('Month')['Sales'].sum().max()


# In[11]:


all_data.groupby('Month', as_index=False)['Sales'].sum().max()


# In[12]:


# Lets plot a graph for our result

months = range(1,13)
plt.figure(figsize=(6,3))
plt.bar(months,total_sales_per_month1['Sales'])
plt.xticks(months)
plt.title('Bar Chart')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)');


# ### Question 2: What city had the highest number of sales?

# In[13]:


all_data


# In[14]:


# lets add our city column
# looking at our dataframe, we can see that we have cities in the purchase address column. So how can we extract it??
# Lets use the apply function
# Notice that the city is between columns, so we split between columns

all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1])
all_data.head()


# In[15]:


result = all_data.groupby('City')['Sales'].sum()
result


# In[16]:


results = all_data.groupby('City', as_index=False)['Sales'].sum()
results


# In[20]:


# Lets plot a graph for our result

city = all_data['City'].unique()
plt.figure(figsize=(6,3))
plt.bar(results['City'], results['Sales'])
plt.xticks(city, rotation='vertical', size=8)
plt.title('Bar Chart')
plt.xlabel('City')
plt.ylabel('Total Sales ($)');


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




