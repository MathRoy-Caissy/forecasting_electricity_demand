# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:34:16 2021

@author: Mathieu
"""

import pandas as pd
import time
import glob
import os
#from datetime import date, timedelta

code_path = os.getcwd()
splitter = code_path.split(sep="\\")
pc_user = splitter[2]

path = code_path.replace("\\", "/")
ROOT_DIR=path
ROOT_DIR

all_files = glob.glob(os.path.join(ROOT_DIR, 'rawdata') + "/*.csv")
    
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

#look for missing times
item_counts = df["Date"].value_counts()

for item in item_counts:
    if item == 24:
        continue
    print(item)

#there are no missing hours and there seems to be no NaN
#or null values anywhere

#fix column names and column types and remove Market Demand (column 2)
# date | Hour | Demand

df.columns = ['date', 'hour', 'market_dem','ontario_dem']
df['date'] = pd.to_datetime(df['date'])

#removing 2 first lines for each file