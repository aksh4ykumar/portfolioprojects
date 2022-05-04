#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None


# In[4]:


#Opening the data in jupyter notebook
df = pd.read_csv (r'C:\Users\Kiba\Desktop\All Here\Practice Datasets\Shark Tank India\shark tank india - Copy.csv')
df


# In[5]:


#Removed the previous column header and promoted the first row of the data to column header. 
df.columns = df.iloc[0]
df = df[1:]
df


# In[6]:


df.head()


# In[7]:


#Creating a new column called Del Status where the column will show if the deal was made or not.
df['Deal Status'] = np.where(df['Deal']!= 'No Deal', 'Yes', 'No')
df.head()


# In[8]:


#Getting column number of 'Deal Status'
df.columns.get_loc("Deal Status")


# In[9]:


#Getting column number of Deal so as to move 'Deal Status' column next to it.
df.columns.get_loc("Deal")


# In[10]:


#Rearranging the columns where now 'Deal Status' is next to 'Deal'
df.insert(7, 'Deal Status', df.pop('Deal Status'))
df.head()


# In[11]:


#Getting the info of the dataset
df.info()


# In[12]:


#this shows the shape of the dataset. 120 rows and 15 columns.
df.shape
#after showing the columns and shape we can see there are some null columns from Ashneer to Ghazal.
#how did i know this? the rows show 120. So there should be 120 non-null entries.
#from Ashneer to Ghazal there arent no 120 non null entries. 


# In[13]:


#to show all the columns in the dataset.
df.columns


# In[14]:


#Checking the number of null values there are in the data caolumsn.
df.isna().sum()


# In[15]:


# Lets find the total number of null values

df.isnull().sum().sum()

print('The total number of null values in the whole dataset is {}.'.format(df.isnull().sum().sum()))


# In[16]:


#checking duplicates in the dataset. The numbers from 1 to 120 are the rows. 
#All are shown flase so there is no duplicate values but if there is then there will be a 'True'
df.duplicated()
#So there are no duplicates in this data. 


# In[17]:


#this is to show if there is any uniqe value
#for example if there is some unique value in a number column which contains text then this function will reveal it. 
df['Brand'].unique()


# In[18]:


# Lets find the total number of null values in a particualr column. in this case it is the 'Idea' column

df['Idea'].isnull().sum()

print('The total number of null values in Idea column is {}.'.format(df['Idea'].isnull().sum()))
# We find out there is no null values. 


# In[19]:


#Replacing all the null values in a column with 0. You can fill it with anything but i choose 0.
df['Ashneer'].fillna(0)
#Replacing all the null values in a column with 'No Investment'.
df['Ashneer'].fillna('No Investment')
#Replacing all the null values in a column with 0. You can fill it with anything but i choose 0.
#Cuurently this code is being run so you will see 0's instead of null values. 
#For other values execute the previous code in this cell. 

#Finnaly, i did not write 'inplace=True' after 0 in the code. 
#If i wanted the changes to take place in the data i should write 'inplace=true'
#For this example i did not so as to show other fillna codes below but if i want to remove the Null/NA colulmns then,
#i should use 'inplace=True' after the 0.
df['Ashneer'].fillna(0)


# In[20]:


#checking if 'Ashneer' column has 0 values
df['Ashneer'].isnull().sum()


# In[21]:


#To replace all the NAN/Null values with 0. I can use anything but for this example i used 0.
#Again if i wanted to make permanent changes i should use 'inplace=True' after the 0 seperated by a comma
df.fillna(0)


# In[22]:


df['Ashneer'].notnull()


# In[23]:


df.head()


# In[24]:


# Getting the column numbers by using df.info()
df.info()


# ### Before this keeps te data in its original form

# In[25]:


# Selecting only the columns that needs to be changed. 
df.iloc[:,8:15]


# In[26]:


#Converting only selected columns to 1 and 0 
df.iloc[:,8:15].eq('yes').mul(1)


# In[27]:


df.replace('yes', 1)


# In[28]:


df


# In[29]:


#Removing additional spaces
df.columns = df.columns.str.replace(' ', '')


# In[30]:


df


# In[31]:


#converting all the Yes to 1. 
df.iloc[:,8:15].eq('yes').mul(1)


# In[32]:


#there was a problem. yes in 'Anupam' column were not reading as 'Yes' so i wanted to check the column.
#also seeing the 'NaN' values.
df['Anupam']


# In[33]:


#checking the total amount of not null values
df['Anupam'].notnull().sum()


# In[34]:


#converting null and not null values to 1s and 0s only on 'Anupam' column.
df['Anupam'] = df['Anupam'].notnull().astype('int')


# In[35]:


#checking the result
df['Anupam']


# In[36]:


df['Anupam'].notnull().sum


# In[37]:


#counting the number of 1s which means true or 'yes' from the dataset.
df['Anupam'].value_counts()[1]


# In[38]:


#if you want to change only specific columns to yes or no.
ndf = df.iloc[:,8:10].notnull().astype('int')


# In[39]:


ndf = df


# In[40]:


ndf = df.iloc[:,8:15].notnull().astype('int')


# In[41]:


ndf


# In[ ]:





# In[42]:


df


# In[43]:


#Creating a new data set with inte values.
wdf = df.notnull().astype('int')


# In[44]:


wdf = df


# In[45]:


df


# In[46]:


# the result i wanted. converting the columns i want from 'yes' and 'NaN' to 1s and 0s
wdf = wdf.iloc[:,8:15].notnull().astype('int')


# In[47]:


wdf['Anupam'].value_counts()[1]


# In[48]:


wdf


# ### Starting New

# In[49]:


# Starting new
df


# In[50]:


wdf = df.notnull().astype('int')


# In[51]:


df


# ### correction happens from here where i make a new dataset wdf with only int values
# ### 1s and 0s as yes or no. 

# In[52]:


wdf = df


# In[53]:


wdf


# In[54]:


df


# In[55]:


wdf = df.notnull().astype('int')


# In[56]:


wdf


# In[ ]:





# ### creating correlation for only Hosts

# In[57]:


wdf.apply(lambda x: x.factorize()[0]).corr(method='pearson')


# In[58]:


correlation_matrix = wdf.apply(lambda x: x.factorize()[0]).corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Shark Tank")

plt.xlabel("Shark Tank features")

plt.ylabel("Shark Tank features")

plt.show()


# In[59]:


wdf


# In[60]:


# now checking the total amount of time hosts invested. 
wdf['Ashneer'].value_counts()[1]


# In[61]:


wdf['Namita'].value_counts()[1]


# In[62]:


wdf['Anupam'].value_counts()[1]


# In[63]:


wdf['Vineeta'].value_counts()[1]


# In[64]:


wdf['Aman'].value_counts()[1]


# In[65]:


wdf['Peyush'].value_counts()[1]


# In[66]:


wdf['Ghazal'].value_counts()[1]


# In[67]:


# creating pie chart for the data
# this shows who is more likely to invest in shark tank
y = np.array([24, 25, 27, 18, 31, 30, 10])
mylabels = ["Ashneer", "Namita", "Anupam", "Vineeta","Aman","Peyush","Ghazal"]

plt.pie(y, labels = mylabels, startangle = 90, autopct='%1.0f%%')
plt.show() 


# In[74]:


#checking out the original data for creating a graph out of deal status
df


# In[75]:


#checking the info of the column
df['DealStatus'].value_counts()


# In[78]:


df['DealStatus'].value_counts().plot(kind='bar')


# ### Finding correlation.

# In[68]:


# now finding the correleation in this dataset as a whole.
# Using factorize - this assigns a random numeric value for each unique categorical value

df.apply(lambda x: x.factorize()[0]).corr(method='pearson')


# In[69]:


correlation_matrix = df.apply(lambda x: x.factorize()[0]).corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Shark Tank")

plt.xlabel("Shark Tank features")

plt.ylabel("Shark Tank features")

plt.show()


# In[70]:


sns.regplot(x="Ashneer", y="Vineeta", data=wdf)


# In[71]:



sns.set_style('whitegrid')
sns.lmplot(x ='Ashneer', y ='Vineeta', data = wdf)


# In[ ]:





# In[ ]:




