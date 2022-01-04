# Last time we saw that Israel spend a lot on R&D, we want to now see how this translates in terms of inequality

# We therefore get data on the Income Gini coefficient and add it to our DataFrame

# Importing the necessaru modules

import world_bank_data as wb
import pandas as pd
import requests

# Adding the data I have already obtained

url = "https://raw.githubusercontent.com/EliezerMeyer/EliezerMeyer.github.io/main/Israeldata.csv"

df1 = pd.read_csv(url)

# Getting the new data from the World Bank API

df2 = pd.DataFrame(wb.get_series('SI.POV.GINI', date='1996:2018', id_or_value='id', country="ISR", simplify_index=True))

# Adding this data to the dataframe
df1.insert(3, "Gini", df2["SI.POV.GINI"].values)

# Cleaning the data

df1 = df1.iloc[: , 1:]
df1.columns=["Research Spending", "Year", "Gini"]
df1 = df1.dropna()

# Saving to be charted

df1.to_csv("Israelinequalitycheck.csv")
