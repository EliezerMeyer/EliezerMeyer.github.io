# To download the financial data in the most efficient and automated way, I will use the yfinance package

import yfinance as yf
import pandas as pd
import numpy as np

# Allowing myself to see the whole dataframe

pd.set_option("display.max_rows", 1000, "display.max_columns", 1000)

# The stocks I want to see figures for (^GSCC is the S&P500 Index)

tickers = ["FB", "AAPL", "AMZN", "GOOGL", "NFLX", "^GSPC"]
start = "2017-01-04"
end = "2022-01-04"


df1 = yf.download(tickers, start, end)["Close"]

# I am changing the column name for the S&P500 index as Vega Lite has difficulty with "&" and "^", so I must put a custom name
df1.columns=["AAPL", "AMZN", "FB", "GOOGL", "NFLX", "SP500"]

# Saving the data to be charted

df1.to_csv(r"C:\Users\meyer\github\EliezerMeyer.github.io\stocks.csv")
