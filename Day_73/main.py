import pandas as pd
from pandas.tseries.offsets import DateOffset
import matplotlib.pyplot as plt

# below code log from jupiter editor (on google disk)

df=pd.read_csv('QueryResults.csv',names=['DATA','LANGUAGE','POSTS'],header=0)
df[['LANGUAGE','POSTS']].groupby('LANGUAGE').sum().sort_values(by='POSTS',ascending=False).head(3)
df[['LANGUAGE','POSTS']].groupby('LANGUAGE').count().head(3).sort_values(by='POSTS',ascending=False)
df['DATA'].describe()
df['month_offset']= df['DATA'].apply(lambda row: (pd.Timestamp.now().to_period('m') - pd.to_datetime(row).to_period('m')).n)
df['DATA'] = pd.to_datetime(df.DATA)
type(df['DATA'][1])
reshaped_df = df.pivot(index='DATA',columns='LANGUAGE', values='POSTS')
reshaped_df.fillna(value = 0, inplace = True)
reshaped_df.head(3)
reshaped_df.isna().values.any()
reshaped_df['python'].plot()
plt.figure(figsize=(12,10),edgecolor='green',facecolor='green')
plt.yticks(size=12)
plt.xticks(size=12)
plt.xlabel(xlabel='_cycki_',fontsize=15)
plt.ylabel(ylabel='_cycki_',fontsize=15)
plt.ylim(0,35000)
# plt.xlim(2008,2012)#
rolled_df = reshaped_df.rolling(window=8).mean()
#for column in reshaped_df.columns:
#  plt.plot(reshaped_df.index, reshaped_df[column], label=reshaped_df[column].name)
for column in rolled_df.columns:
  plt.plot(rolled_df.index, rolled_df[column], label=rolled_df[column].name)
plt.legend(loc='upper left')
plt.plot(reshaped_df[['javascript','python','assembly','c#']], label=['javascript','python','assembly','c#'])
plt.legend()


'''
Learning Points & Summary
Congratulations on completing another challenging data science project! Today we've seen how to grab some raw data and create some interesting charts using Pandas and Matplotlib. We've

used .groupby() to explore the number of posts and entries per programming language

converted strings to Datetime objects with to_datetime() for easier plotting

reshaped our DataFrame by converting categories to columns using .pivot()

used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()

created (multiple) line charts using .plot() with a for-loop

styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.

added a legend to tell apart which line is which by colour

smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.


Well done for completing today's lessons! Have a good rest. I'll see you tomorrow! 
'''