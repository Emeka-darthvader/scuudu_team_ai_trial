import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
sns.set()

births = pd.read_csv("data/births.csv")
print(births.head()) # we see the number of male births outnumber the female ones


births['day'].fillna(0, inplace=True) #fill in the NA fields as 0 i think
births['day'] = births['day'].astype(int) #set type as int
births['decade'] = 10 * (births['year'] // 10) #do the integer division of all years in birth and multiple by 10 to get the decade
births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
print(births.head())

#visualise
birth_decade = births.pivot_table('births', index='decade', columns='gender', aggfunc='sum') 
birth_decade.plot() 
plt.ylabel("Total births per year") 
plt.show()

#####Further Exploration

#remove outliers
quartiles = np.percentile(births['births'], [25, 50, 75])
mean = quartiles[1]
sigma = 0.74 * (quartiles[2] - quartiles[0])

#using query to filter out the values
births = births.query('(births &gt; @mean - 5 * @sigma) &amp; (births &lt; @mean + 5 * @sigma)') 
births.index = pd.to_datetime(10000 * births.year + 100 * births.month + births.day, format='%Y%m%d') 
births['day of week'] = births.index.dayofweek

#plot births by weekday
births_day = births.pivot_table('births', index='day of week',columns='decade', aggfunc='mean')
births_day.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
births_day.plot()
plt.ylabel("Average Births by Day")
plt.show()