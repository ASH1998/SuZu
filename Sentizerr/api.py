import streamlit as st
import pandas as pd
import tqdm
import time
import matplotlib.pyplot as plt
import numpy as np

from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override()

st.title('NSE Stock')

df = pd.read_csv("IndiaNSE.csv")

st.table(df.iloc[0:10])


stocknames = df['NAME']
stocknames = ['Select Stock : '] + list(stocknames)
selection = st.selectbox("Select Intended Stock : ", stocknames)

if selection!='Select Stock : ':
    # st.write('You selected:', format_text(option, 0, len(option)))
    st.write('Selected File Name:', selection)
    res = df[df['NAME']==selection]
    st.dataframe(res)

    with st.spinner("Fetching Data..."):
        data = pdr.get_data_yahoo(str(res['YCODE'].iloc[0]), start="2017-01-01", end="2021-04-17")

        st.dataframe(data.tail(10))

        st.line_chart(data['Open'])
        # st.line_chart(data['High'])

# with st.spinner(text='In progress'):
#     time.sleep(5)
#     st.success('Done')

# st.balloons()


arr = np.random.normal(1, 1, size=100)

fig, ax = plt.subplots()

palette = plt.get_cmap('Set1')
num = 0
resnew = data.drop('Volume', axis=1)
for column in resnew.columns:
    num+=1
    plt.plot(data[column], marker='', color=palette(num), label=column)
# plt.legend

st.pyplot(fig)