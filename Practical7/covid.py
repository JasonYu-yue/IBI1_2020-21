import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#The code for importing the .csv file works
os.chdir("C:\Users\86157\Desktop\VS code\IBI practical7")
covid_data = pd.read_csv("full_data.csv")
#There is correct code for showing all columns, and every second row between (and 
#including) 0 and 10
print('The code for showing all columns, and every second row between (and including) 0 and 10')
print(covid_data.iloc[0:12:2,0:6])
#Used a Boolean to show “total cases” for all rows corresponding
#to Afghanistan.
print('used a Boolean to show “total cases” for all rows corresponding to Afghanistan')
print(covid_data.loc[covid_data["location"] == "Afghanistan", "total_cases"])
#Computed the mean and median of new cases for the entire world
mean = str(np.mean(covid_data.loc[7880:7971,"new_cases"]))
median = str(np.median(covid_data.loc[7880:7971,"new_cases"]))
print('the mean of the new cases for the entire world:',mean)
print('the median of the new cases for the entire world:', median)
plot=covid_data.loc[7880:7971,"new_cases"]
#Created a boxplot of new cases worldwide.
#The code is applied from the week6.1 lecture
plt.boxplot(plot,
	vert = True,
	whis = 1.5,
	patch_artist = True,
	meanline = False,
    showbox = True,
	showcaps = True,
	showfliers = True,
	notch = False
	  )
plt.titile('the new cases of the covid-19')
plt.show()
plt.xlable('worldwild_situation')
plt.ylable('the number of the world_new_cases')
#plotted both new cases and new deaths worldwide
#locate the data first
world_new_cases = covid_data.loc[covid_data.loc[:,'location'] == "World", 'new_cases']
world_new_deaths = covid_data.loc[covid_data.loc[:,'location'] == "World", 'new_deaths']
world_date = covid_data.loc[covid_data["location"] == "World","date"]
#plot the data
plt.plot(world_date, world_new_cases, 'b.', label = 'world_new_cases',colour = 'blue')
plt.plot(world_date, world_new_deaths, 'r+', label = 'world_new_deaths',colour = 'red')
#I applied the following code form the practical material
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.title('the new cases and the new deaths of covid-19 worldwilde')
plt.xlable('date')
plt.ylabel('the number of new cases or new deaths')
plt.show()
#There is code to answer the question stated in file question.txt
#my question is what is the situation of the total_cases and total_deaths in Afghanistan
#The code to answer the question runs without errors
#The code to answer the question does what it is meant to do
world_date = covid_data.loc[covid_data.loc[:,'location'] == "World", 'date']
Afghanistan_total_deaths = covid_data.loc[0:81,"total_deaths"]
Afghanistan_total_cases = covid_data.loc[covid_data.loc[:,"location"] == "Afghanistan",'total_cases']
plt.plot(world_date,Afghanistan_total_cases, color = 'red',lable = 'total_cases')
plt.xlabel= 'date'
plt.ylabel= 'Afghanistan total cases'
plt.plot(world_date,Afghanistan_total_deaths, color = 'blue',label = 'total_deaths')
plt.xlabel='date'
plt.ylabel='Afghanistan total deaths'
plt.title('the Afghanistan total cases and deaths of the covid-19')
plt.legend()
plt.show()
#the meaning of the code:
print('the meaning of the code is that we found that the total cases occurs at 2020-2-25 and grow fastly through the time')
print('the meaning of the code is that we found that the total cases occurs at 2020-3-24 and grow slowly through the time')
