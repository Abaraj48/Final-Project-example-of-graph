
# coding: utf-8

# In[1]:


import os 
os.getcwd()


# In[128]:


file= 'C:\\Users\\andre\Documents\Average high and low tempratures Victorvill.csv'
File66= 'C:\\Users\\andre\Documents\Modesto  and LA  Monthly crime.csv'


# In[129]:


import numpy as np
data = np.genfromtxt(file,skip_header=0,delimiter=',')
datta = np.genfromtxt(File66,skip_header=0,delimiter=',')


# In[139]:


MM= datta[:,1]
MMM= datta[:,2]
MMMM= datta[:,3]
LL = UU[:,5]


# In[145]:


pyplot.plot(MM)


# In[144]:


pyplot.plot(LL,MM,'.')


# In[138]:


pyplot.plot(MMM)


# In[43]:


data


# In[44]:


y = data[:,2]


# In[45]:


y


# In[46]:


import math 
from matplotlib import pyplot


# In[47]:


pyplot.plot(y,'r',x,'*')
pyplot.xlabel('Months')
pyplot.ylabel('Average High and Low Temprature')
pyplot.title('Annual Temprature')
pyplot.legend('-')


# In[48]:


x = data[:,1]


# In[49]:


file2= 'C:\\Users\\andre\Documents\Victorville CA crime rate.csv'


# In[50]:


data2=np.genfromtxt(file2,skip_header=0,delimiter=',')


# In[51]:


data2


# In[52]:


Y = data2[:,2]
X = data2[:,1]


# In[53]:


pyplot.plot(X,Y,)
pyplot.xlabel('Months')
pyplot.ylabel('Reported Crimes')
pyplot.title('Monthly Crime Rate Victorville')


# In[54]:


## atc edit

pyplot.plot(y,'r',x,'*')
pyplot.plot(X,Y*max(y)/max(Y),)
pyplot.xlabel('Months')
pyplot.ylabel('Average High and Low Temprature')
pyplot.title('Annual Temprature')
pyplot.legend('-')


# In[55]:


pyplot.plot(Y,y,'*')
pyplot.legend('*')
pyplot.xlabel('Crime Rate')
pyplot.ylabel('Temprature')


# In[56]:


import numpy as np 


# In[57]:


file2 = 'C:\\Users\\andre\\Documents\\Top 12 Cities for crime.csv'


# In[58]:


qq = np.genfromtxt(file2,skip_header=1, delimiter=',')


# In[59]:


qq


# In[60]:


w = qq[:,0]
# Population of the cities 
ww= qq[:,2]
# Property crimes per city 


# In[61]:


w


# In[62]:


ww


# In[63]:


def Volume_percrime():
    return (ww/w)*1000
# a function that takes in the number of property crimes divided by the population of the city and multiplies by 1000
# Provides the volume of crimes per 1000 people 


# In[64]:


Volume_Propertycrime= Volume_percrime()


# In[65]:


Volume_Propertycrime


# In[66]:


Volume_Propertycrime.max()


# In[67]:


Volume_Propertycrime.min()


# In[68]:


R = np.sort(Volume_Propertycrime)


# In[69]:


file3 = 'C:\\Users\\andre\\Documents\\Safe cities.csv'


# In[70]:


safe = np.genfromtxt(file3,skip_header= 1, delimiter= ',')


# In[71]:


safe


# In[72]:


a= safe[:,0]
b = safe[:,2]


# In[73]:


def Volume_percrime1():
    return (b/a)*1000


# In[74]:


f = Volume_percrime1()


# In[75]:


f


# In[76]:


L= np.sort(f)


# In[77]:


L


# In[78]:


pyplot.hist(R)
pyplot.hist(L)
pyplot.xlabel('Property Crime per 1000')
pyplot.ylabel('Number of Cities')
pyplot.legend('HL')
# H is for the blue high crime 
# L is for low crime 


# In[79]:


file4 = 'C:\\Users\\andre\\Documents\\San Bernandino Weather .csv'


# In[80]:


SBW = np.genfromtxt(file4,delimiter=',')


# In[81]:


SBWW = SBW[:,0]


# In[82]:


SBWW


# In[92]:


pyplot.plot(y,'red',SBWW,'blue', WW, 'g')
pyplot.xlabel('Months')
pyplot.ylabel('Average High in F')
pyplot.legend('VSI')


# In[104]:


file5 = 'C:\\Users\\andre\\Documents\\Different Weathers.csv'


# In[105]:


WW = np.genfromtxt(file5,skip_header= 1, delimiter= ',')


# In[106]:


WW


# In[107]:


file6 = 'C:\\Users\\andre\\Documents\\High crime weather.csv'


# In[108]:


UU = np.genfromtxt(file6,skip_header= 1, delimiter= ',')


# In[116]:


pyplot.plot(UU,'b',WW,'r')


# In[110]:


pyplot.plot(UU,'r')
pyplot.legend('123456789')


# In[111]:


pyplot.plot(WW)

