
# coding: utf-8

# In[2]:


import math 
from matplotlib import pyplot
import numpy as np
import os
# These are the main imports for my project


# In[54]:


os.getcwd()
# Obtaining the user name 
# This indicates where we are at once obtain this then we just need to find out where we saved the data and the name of the data


# In[80]:


# Files I need to import  under.csv
file1='C:\\Users\\andre\Documents\Different Weathers.csv'
# This file contains the safe cities monthly average weather.
file2='C:\\Users\\andre\Documents\High crime weather.csv'
# This file contains the average monthly weather of the cities with high crime. 
file3='C:\\Users\\andre\Documents\Modesto Monthly crime.csv'
# The city of Modesto's average crime rates for the 2015.
file4='C:\\Users\\andre\Documents\Average high and low tempratures Victorvill.csv'
# Average crime rates per month for Victorville CA.
file5= 'C:\\Users\\andre\Documents\Victorville CA crime rate.csv'
# The city of Victorville's average crime rates for 2011


# Now I will define the imported data of the file using np.genfromtxt
data1 = np.genfromtxt(file1,skip_header=1,delimiter=',')
# Skip_header = 1 means we are skipping the first row of the data
# This is because the first row is just words,so no numerical values.Which means, they cant be used or measured to find results.
data2 = np.genfromtxt(file2, skip_header=1,delimiter=',')
data3= np.genfromtxt(file3, skip_header=0,delimiter=',')
data4= np.genfromtxt(file4,skip_header=0,delimiter=',')
data5=np.genfromtxt(file5,skip_header=0,delimiter=',')


# In[81]:


data1
# Checking to see that each data was properly imported as arrays of data


# In[82]:


data2


# In[83]:


data3


# In[84]:


data4


# In[85]:


NumberofcrimesModesto= data3[:,1]
# [:,1] the right of the comma isolates the column and the left of the comma isolates the row
# Here I am isolating and defining the number of crimes from January to December in Modesto CA


# In[86]:


pyplot.plot(NumberofcrimesModesto)
# I am creating a plot of the isolated data, adding a title,x and y axis labels.
pyplot.xlabel('Months')
pyplot.ylabel('Number of Crimes Reported')
pyplot.title('Monthly Crime Rate Modesto')


# In[87]:


MW = data2[:,5]
# This column reprsents the average monthly weather 


# In[88]:


pyplot.plot(MW,'g')
pyplot.xlabel('Months')
pyplot.ylabel('Temprature in Fahrenheit')
pyplot.title('Monthly Average Weather Modesto')


# In[96]:


pyplot.plot(MW,NumberofcrimesModesto,'.')


# In[102]:


np.polyfit(MW,NumberofcrimesModesto,1)
# I need to apply a linear equation to create a fitted line.
# I use np.polyfit
# It returns an array that contains a slope(1.12489613) and the y-intercept is 110.62667041
# the values found for y =mMW+b tells me that as the temprature in fahrenheit increases the number crimes reported starting at 110 increases by 1.12


# In[143]:


# The linear equation y = mx+b
# I define m,b as the poly fit that provides me the slope y-intercepy
m, b = np.polyfit(MW,NumberofcrimesModesto,1)
pyplot.plot(MW,b+m*MW,'-')
# I apply the linear equation with the x axis, which in this case is Modesto's monthly weather.
# Plot the x axis and y = mMW+b
pyplot.plot(MW,NumberofcrimesModesto,'.')
# Plot the Monthly weather and crime rates
pyplot.xlabel('Average Temprature in Fahrenheit')
pyplot.ylabel('Number of Crimes Reported')
pyplot.title('Modesto Temprature vs Number of Crimes')
pyplot.legend('FD')
# F is for fitted function and D is for Data


# In[50]:


Number_of_crimes_Victorville= data5[:,2]
# Here I am isolating and defining the number of crimes from January to December in Victorville CA


# In[51]:


pyplot.plot(Number_of_crimes_Victorville,'y')
# I am plotting the data and making the color of the line yellow
pyplot.xlabel('Months')
pyplot.ylabel('Number of Reported Crimes')
pyplot.title('Monthly Crime Rate Victorville')


# In[52]:


VW = data4[:,2]
# Victorville's average montlhy weather
pyplot.plot(VW,'r')
pyplot.xlabel('Months')
pyplot.ylabel('Temprature in Fahrenheit')
pyplot.title('Monthly Average Weather Victorville')


# In[141]:


np.polyfit(VW,Number_of_crimes_Victorville,1)


# In[144]:


mm, bb = np.polyfit(VW,Number_of_crimes_Victorville,1)
pyplot.plot(VW,bb+mm*VW,'-')
pyplot.plot(VW,Number_of_crimes_Victorville,'^')
pyplot.xlabel('Average Temprature in Fahrenheit')
pyplot.ylabel('Number of Crimes Reported')
pyplot.title('Victorville Temprature vs Number of Crimes')
pyplot.legend('FD')
# F for fitted function and D for the data
# Tells me that as the temprature in fahrenheit increases the number crimes reported, which starts at 807, increases by 4.8.


# In[149]:


pyplot.plot(data1,'b')
# Plotting the safe cities average monthly weather.
pyplot.xlabel('Months')
pyplot.ylabel('Temprature in Fahrenheit')
pyplot.title('Safe Cities Monthly Average Weather')
# This shows that most cities go no higher then the mid 80's. During summer the range goes from mid 70's to mid 80's.
# Lincoln is the only one that goes beyond 90 degrees during the summer.It's located near Sacramento.


# In[152]:


pyplot.plot(data2,'g')
# Plotting the more dangerous cities average monthly weather.Also the usual x and y labels and title.
pyplot.xlabel('Months')
pyplot.ylabel('Temprature in Fahrenheit')
pyplot.title('Dangerous Cities Monthly Average Weather')
# Most of the cities go up to 90 or above during the summer.The range is  from 90 to 100
# The three cities with very low calm average tempratures is Salinas, Oakland, and Vallejo.
# Salinas is up north near San Jose, Oakland and Vallejo are both by the bay area. 


# In[154]:


pyplot.plot(data1,'b',data2,'g')
# Plotting all the cities together to get a better view on how their average tempratures are different.
pyplot.xlabel('Months')
pyplot.ylabel('Temprature in Fahrenheit')
pyplot.title('All the Cities Monthly Average Weather')

