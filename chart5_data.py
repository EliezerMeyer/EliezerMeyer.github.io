import yfinance as yf
import pandas as pd
import numpy as np

pd.set_option("display.max_rows", 1000, "display.max_columns", 1000)

tickers = ["FB", "AAPL", "AMZN", "NFLX", "GOOGL"]
start = "2017-01-04"
end = "2022-01-04"

df1 = yf.download(tickers, start, end)["Close"]
print(df1)

df1.to_csv(r"C:\Users\meyer\github\EliezerMeyer.github.io\stocks.csv")
