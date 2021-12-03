# Importing requests so Python can capture data from my raw github
import requests

# Importing pandas to make data tables
import pandas as pd

# Getting pandas to make a dataframe from the unemployment data uploaded to my github

url1 = "https://raw.githubusercontent.com/EliezerMeyer/EliezerMeyer.github.io/main/England%20Unemployment%20Data.csv"
unemploymentdata = pd.read_csv(url1)
df1 = pd.DataFrame(unemploymentdata)
print(df1)

# Getting pandas to make a dataframe from the homelessness data uploaded to my github

url2 = "https://raw.githubusercontent.com/EliezerMeyer/EliezerMeyer.github.io/main/England%20Homlessness%20Data.csv"
homelessnessdata = pd.read_csv(url2)
df2 = pd.DataFrame(homelessnessdata)
print(df2)

# Performing the data join
df3 = df1.join(df2,rsuffix="_right")

# Changing the settings in pandas so I can see the whole dataframe to confirm whether the task has been done right

pd.set_option("display.max_rows", None, "display.max_columns", None)
print (df3)
