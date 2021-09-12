import time
import requests
import numpy as np
import pandas as pd

# 必須先安裝yfinance套件
import yfinance as yf
import h5py

# link = 'https://quality.data.gov.tw/dq_download_json.php?nid=11549&md5_url=bb878d47ffbe7b83bfc1b41d0b24946e'
# r = requests.get(link)
# data = pd.DataFrame(r.json())
save_path = """C:\\Users\\AbrahamChen\\Desktop\\test"""
# data.to_csv(save_path + '/stock_id.csv', index=False, header=True)


# 讀取csv檔
stock_list = pd.read_csv(save_path + '/stock_id.csv')
stock_list.columns = ['STOCK_ID', 'NAME']

historical_data = pd.DataFrame()

for i in stock_list.index:
    # 抓取股票資料
    # stock_id = str(stock_list.loc[i, 'STOCK_ID']) + '.TW'
    stock_id = str('0050') + '.TW'
    data = yf.Ticker(stock_id)
    df = data.history(period="max")
    # 增加股票代號
    df['STOCK_ID'] = stock_list.loc[i, 'STOCK_ID']
    # 合併
    historical_data = pd.concat([historical_data, df])
    time.sleep(0.8)

historical_data.to_hdf(save_path + '/historical_data.h5', key='s')

# HDF5的讀取：
data = pd.read_hdf(save_path + '/historical_data.h5', key='s')
print(data)

