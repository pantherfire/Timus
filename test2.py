'''
Created on Feb 2, 2018

@author: root
'''
import math
import pandas as pd
import numpy as np
import tushare as ts
import datetime
import matplotlib.pyplot as plt
import stockstats

begin_time = '2017-02-01'
end_time = '2017-11-01'
code = "000001"
stock = ts.get_k_data(code, start=begin_time, end=end_time)
stock["date"] = stock.index.values #??????
stock = stock.sort_index(0) # ???????????
#print(stock) [186 rows x 14 columns]
#??????
#stockStat = stockstats.StockDataFrame.retype(pd.read_csv('002032.csv'))
stockStat = stockstats.StockDataFrame.retype(stock)
print(stockStat)
print("init finish .")


stockStat[['volume','volume_delta']].plot(figsize=(20,10), grid=True)
plt.show()
#????delta?????????volume_delta???????
stockStat[['close','close_delta']].plot(subplots=True, figsize=(20,10), grid=True)
plt.show()