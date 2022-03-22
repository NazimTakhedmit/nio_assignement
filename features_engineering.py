import pandas as pd 
import numpy as np 
import os 
import shutil
from support_functions import Challenge_tools as ct
import sys

raw_data_name = str(sys.argv[1])
data = pd.read_csv(raw_data_name)

# remove rows containing nones
data = data.dropna()


'''
   Features selection 
'''
# select the columns which can serve as input for the call volume forecast, namely: Datetime. 

cols = ['Datetime']
data = data[cols]

'''
   Date conversion and date components columns creation
'''

data['Datetime_formatted'] = pd.to_datetime(data['Datetime'])

data['hour'] = data['Datetime_formatted'].apply(lambda x:x.hour)
data['day'] = data['Datetime_formatted'].apply(lambda x:x.day)
data['month'] = data['Datetime_formatted'].apply(lambda x:x.month)
data['year'] = data['Datetime_formatted'].apply(lambda x:x.year)
data['date'] = data['Datetime_formatted'].apply(lambda x:x.strftime('%d/%m/%Y'))

print('date column split  ----Done')

'''
   Add season
'''
# we use the function 'get_season' from the imported package support_functions package

data['season'] = data['Datetime_formatted'].apply(lambda x:ct.get_season(x))
print('adding season column ----Done')

'''
   Add number of calls per day
'''

calls_per_day = data.groupby(['year','month','day']).size().reset_index(name='calls_per_day')

data_call_day = pd.merge(data,calls_per_day,on=['year','month','day'],how='left')

print('adding the number of calls per day column ----Done')
'''
   Add number of calls per hour
'''

calls_per_hour = data.groupby(['year','month','day','hour']).size().reset_index(name='calls_per_hour')

data_call_day_hour = pd.merge(data_call_day,calls_per_hour,on=['year','month','day','hour'],how='left')

print('adding the number of calls per hour column ----Done')
'''
   Save clean data
'''

clean_cols = ['hour','day','month','year','date','season','calls_per_day','calls_per_hour']

clean_data = data_call_day_hour[clean_cols]

clean_data.to_csv('clean_data.csv', index=False)  
print('saving clean data ----Done')











