
# coding: utf-8

# In[122]:


import math 
from matplotlib import pyplot
import numpy as np
import os


# In[36]:


os.getcwd()
# Obtaining the user name 


# In[37]:


# Files I need to import  under.csv
file1 = 'C:\\Users\\andre\\Documents\\Top Cities for crime.csv'
file2 = 'C:\\Users\\andre\\Documents\\Safe cities.csv'
# Now I will define the imported data of the file using np.genfromtxt
data1 = np.genfromtxt(file1,skip_header= 1, delimiter= ',')
data2= np.genfromtxt(file2,skip_header=1, delimiter=',')
# Skip_header = 1 means we are skipping the first row of the data
# This is because the first row is just words,so no numerical values.Which means, they cant be used or measured


# In[38]:


data1
# Checking to see that each data was properly imported as arrays of data


# In[39]:


data2


# In[40]:


# [:,0] the right of the comma isolates the column and the left of the comma isolates the row
HCP=data1[:,0]
# Isolating the column for population size for high crime cities.
HCV=data1[:,1]
# This is the column for number of crime violent crimes for crime cities
HCPC=data1[:,2]
# This is the column for the number of property crimes for high crime cities
LCP=data2[:,0]
# Isolating the column for population size for low crime cities
LCV=data2[:,1]
# This is the column for number of crime violent crimes for low crime cities
LCPC=data2[:,2]
# This is the column for the number of property crimes for low crime cities


# In[41]:


def function1():
# Called my function, function1 and I did not put in any inputs since I already had the values defined outside the function
    return (HCPC/HCP)*1000
# It will return this equation, which provides me the number of people out of a 1000 that were hit by a property crime 
# I divided number of property crimes by the population size of the city and multiplied by 1000


# In[42]:


L = function1()
# Calling the function that is defined by L


# In[43]:


L
# Gives me the results


# In[58]:


np.max(L)
# np.max helps show me what is the maximum value


# In[44]:


np.sort(L)
# I use np.sort to put the number in order from least to greatest


# In[89]:


Property_crime1_per1000={'Adelanto':28.42932777,'Victorville':34.22378163,'Salinas':34.39020945,'Antioch':41.71089838,'San Bernardino':43.80791519,'Bakersfield':46.4656123,'Vallejo':48.45524608,'Modesto':48.90527388,'Stockton':50.30087126,'Oakland':62.33426676}
# I created a dictionary named Property_crime1_per1000.
# The syntax {} is used to create dictionaries 
# The numbers are the values of the keys


# In[90]:


Property_crime1_per1000
# Checking to see if it works
# I can see how many property crimes are commited for every 1000 residents in each city.
#Using the np.max value found I can use to determine which city in my dictionary has thats value, which is Oakland. 


# In[54]:


Property_crime1_per1000['Salinas']
# Checking Salinas numerical value


# In[59]:


def function2():
    return (HCV/HCP)*1000
# This is the same equation as above and one that I will use for the rest.
# The funciton tells me what are the chances of experiencing a violent crime out of 1000 people in the higher crim rate cities.


# In[62]:


LL = function2()
# I am calling the function


# In[64]:


LL


# In[86]:


np.sort(LL)
# Sorting the values


# In[125]:


np.max(LL)
# Finding the max value


# In[92]:


Violent_crime1_per1000={'Adelanto':6.35328092,'Victorville':5.34926335,'Salinas':6.42729643,'Antioch':8.88705177,'San Bernardino':9.09379345,'Bakersfield':5.13183312,'Vallejo':8.61107355,'Modesto':8.34263557,'Stockton':12.08154879,'Oakland':19.76790538}


# In[93]:


Violent_crime1_per1000


# In[95]:


def function3():
    return(LCPC/LCP)*1000
# Function to find the number of people that were hit a property crime in the lower crime rate cities.


# In[99]:


P=function3()
# Calling the function


# In[102]:


P


# In[100]:


np.sort(P)


# In[101]:


np.max(P)


# In[104]:


Property_crime2_per1000 = {'Rancho Santa Margarita':5.89550722,'Aliso Viejo':6.29937006,'Laguna Woods':7.95947902,'Danville':9.51371772,'Laguna Niguel':9.61568096,'San Ramon':10.21038773,'Mission Viejo':10.40721623,'Los Altos':11.84449959,'Lincoln':12.33521447,'Irvine':13.92952551}


# In[105]:


Property_crime2_per1000
# I created a dictionary for the values of lower crime rate cities.


# In[106]:


def function4():
    return(LCV/LCP)*1000
# Number of violent crimes out of 1000 people for lower crime rate cities. 


# In[107]:


PP=function4()


# In[108]:


PP


# In[111]:


np.min(PP)
# The number is very small.
# All the values are very small.


# In[128]:


np.max(PP)
# Even the max value does not reach the number 1


# In[110]:


Violent_crime2_per1000 = {'Rancho Santa Margarita':0.3455987,'Aliso Viejo':0.49995,'Laguna Woods':0.30149542,'Danville':0.39160581,'Laguna Niguel':0.87835547,'San Ramon':0.36273746,'Mission Viejo':0.64654049,'Los Altos':0.76095947,'Lincoln':0.55764984,'Irvine':0.47915872}


# In[112]:


Violent_crime2_per1000
# Dictionary for low crime rate cities for violent crime.


# In[130]:


pyplot.hist(L)
pyplot.hist(P)
# I am plotting the number of property crimes for both low and high crime rate cities.
# This histogram will demonstrate how the chances of being hit with a property crime are very different for both.
pyplot.xlabel('Property Crime per 1000')
pyplot.ylabel('Number of Cities')
pyplot.legend('HL')
pyplot.title('Low Crime vs High Crime Cities')
# H is for the blue high crime cities
# L is for low crime cities


# In[134]:


pyplot.hist(LL)
pyplot.hist(PP)
# Plotting the chances of being hit with a violent crime for high and low crime cities
# Again showing the large differences
pyplot.xlabel('Violent Crime per 1000')
pyplot.ylabel('Number of Cities')
pyplot.legend('HL')
pyplot.title('Low Crime vs High Crime Cities')


# In[136]:


Total1= L+LL
Total2=P+PP
# Adding the property and violent crimes per 1000 people together for both the low and high crime cities.
# I will be the total for crimes per 1000 for low and high crime cities.
#Defining the totals  as Total1 and Total2


# In[138]:


pyplot.hist(Total1)
pyplot.hist(Total2)
# Plotting the histograms for both high and low crime cities
# Agaian demonstrating the differences
pyplot.xlabel('Total Crimes per 1000')
pyplot.ylabel('Number of Cities')
pyplot.legend('HL')
pyplot.title('Low Crime vs High Crime Cities')

