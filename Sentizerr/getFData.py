from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe using pandas_datareader
data = pdr.get_data_yahoo("AJMERA.NS", start="2017-01-01", end="2021-04-17")
print(data.tail())
print(data.shape)
data.to_csv("APPL today.csv")