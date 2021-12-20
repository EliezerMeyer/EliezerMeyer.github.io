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

# Time for advanced analytics

# Importing helpful libraries

import matplotlib.pyplot as plt
import numpy as np

# Making it easier to plot the data

x = df3["Year"].values
y1 = df3[df3.columns[1]]
y2 = df3[df3.columns[3]]

# Importing Searborn

import seaborn as sns

# Making sure the final figure is a size that matches my other charts

sns.set(rc = {'figure.figsize': (5.729,5.729)})

# Running a regression to see the relationship between the unemployment rate and the number of people who had to sleep rough one night in Autumn in England

sns.regplot(x=y1, y=y2)
plt.xlabel('Unemployment Rate (%)', size=12)
plt.ylabel('Number of People Homeless for at least one night in Autumn', size=12)
plt.title('Unemployment and Homelessness')
plt.savefig(r'C:\Users\meyer\github\EliezerMeyer.github.io\Homework9_regressionimage.png')
