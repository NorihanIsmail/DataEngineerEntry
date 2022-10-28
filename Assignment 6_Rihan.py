# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 12:18:29 2022

@author: norihan
"""

#ASSIGMENT 6: PACKAGES

#No.1:For the dataset “Indian_cities”, 
#a)Find out top 10 states in female-male sex ratio
#b)Find out top 10 cities in total number of graduates
#c)Find out top 10 cities and their locations in respect of  total effective_literacy_rate.


import pandas as pd

data=pd.read_csv("C:/Users/norihan/Desktop/DS/DG360/Python Programming/Assignment/Module6_Indian_cities.csv")
data.nlargest(10,['sex_ratio'])

data.nlargest(10,['total_graduates'])

data.nlargest(10,['effective_literacy_rate_total'])

#No.2:For the data set “Indian_cities”
#a)Construct histogram on literates_total and comment about the inferences
#b)Construct scatter  plot between  male graduates and female graduates

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

data=pd.read_csv("C:/Users/norihan/Desktop/DS/DG360/Python Programming/Assignment/Module6_Indian_cities.csv")
data.hist('literates_total')
data.literates_total.describe()


plt.scatter(data['male_graduates'],data['female_graduates']);plt.ylabel("Male & Female Graduates")



#No.3:For the data set “Indian_cities”
#a)Construct Boxplot on total effective literacy rate and draw inferences
#b)Find out the number of null values in each column of the dataset and delete them.

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/norihan/Desktop/DS/DG360/Python Programming/Assignment/Module6_Indian_cities.csv")
plt.boxplot(data['effective_literacy_rate_total']);plt.ylabel("effective_literacy_rate_total") 
data.effective_literacy_rate_total.describe()


print(data.isnull())
data.isnull().sum()
data.dropnull()

#Comment from trainers
plt.boxplot(indianCities['effective_literacy_rate_total']) 
plt.ylabel("Total Effective Literacy Rate") 
print("Inference: Most Indian cities have a high total effective literacy rate in the range of 80% to 90%") 

df = pd.DataFrame(indianCities) 
for i in range(len(df.index)): 
    print(f"Total NaN in row {i+1}: ", df.iloc[i].isnull().sum())

