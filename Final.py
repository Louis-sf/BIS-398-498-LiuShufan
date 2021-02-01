# -*- coding: utf-8 -*-

import pandas as pd

YT2019 = pd.read_csv("yellow_tripdata_2019-06.csv")

YT2020 = pd.read_csv("yellow_tripdata_2020-06.csv")

# Curation for YT2019:
    
# trip_distance <= 100
YT2019['valid'] = YT2019['trip_distance'] <= 100

YT2019[['trip_distance','valid']].head()

YT2019['trip_distance'].describe()

YT2019 = YT2019[YT2019.valid == True]    

# delete any rows where passengers = 0 
YT2019['valid'] = YT2019['passenger_count'] != 0
YT2019 = YT2019[YT2019.valid == True]    

# delete trip distance = 0
YT2019['valid'] = YT2019['trip_distance'] != 0
YT2019 = YT2019[YT2019.valid == True]  


# for total_amount make greater than zero but less than 1,000
YT2019['total_amount'].describe()
YT2019['valid'] = YT2019['total_amount'] > 0
YT2019 = YT2019[YT2019.valid == True]
YT2019['valid'] = YT2019['total_amount'] < 1000
YT2019 = YT2019[YT2019.valid == True]
# make "extra" >= 0
YT2019['extra'].describe()
YT2019['valid'] = YT2019['extra'] >= 0
YT2019 = YT2019[YT2019.valid == True]
YT2019.to_csv('Yellow2019-6_Saved.csv', index = False)

# Curation for YT2020:
# trip_distance <= 100
YT2020['valid'] = YT2020['trip_distance'] <= 100

YT2020[['trip_distance','valid']].head()

YT2020['trip_distance'].describe()

YT2020 = YT2020[YT2020.valid == True]    

# delete any rows where passengers = 0 
YT2020['valid'] = YT2020['passenger_count'] != 0
YT2020 = YT2020[YT2020.valid == True]    

# delete trip distance = 0
YT2020['valid'] = YT2020['trip_distance'] != 0
YT2020 = YT2020[YT2020.valid == True]  


# for total_amount make greater than zero but less than 1,000
YT2020['total_amount'].describe()
YT2020['valid'] = YT2020['total_amount'] > 0
YT2020 = YT2020[YT2020.valid == True]
YT2020['valid'] = YT2020['total_amount'] < 1000
YT2020 = YT2020[YT2020.valid == True]
# make "extra" >= 0
YT2020['extra'].describe()
YT2020['valid'] = YT2020['extra'] >= 0
YT2020 = YT2020[YT2020.valid == True]
YT2020.to_csv('Yellow2020-6_Saved.csv', index = False)

#Compare means
#2019:
trip_distance_mean2019 = YT2019['trip_distance'].mean()
passenger_count_mean2019 = YT2019['passenger_count'].mean()
total_amount_mean2019 = YT2019['total_amount'].mean()
extra_mean2019 = YT2019['extra'].mean()
#2020:
trip_distance_mean2020 = YT2020['trip_distance'].mean()
passenger_count_mean2020 = YT2020['passenger_count'].mean()
total_amount_mean2020 = YT2020['total_amount'].mean()
extra_mean2020 = YT2020['extra'].mean()

import numpy as np

means2019 = np.array([trip_distance_mean2019,passenger_count_mean2019,
                     total_amount_mean2019,extra_mean2019])
means2020 = np.array([trip_distance_mean2020,passenger_count_mean2020,
                     total_amount_mean2020,extra_mean2020])

print('\t  tripdistance\tpassenger\ttotal\t   extra')
print('2019:',means2019)
print('2020:',means2020)