# For this chart I will use Nobel Prize Winners Per Capita as a proxy for innovation
# I will therfore scrape Nobel Prize and population data
# I will then obtain income gini data
# I will then put all that data into a csv file to graph and find a relationship

# Importing packages for data manipulation

import pandas as pd
import numpy as np

# packages for scraping

import requests
from bs4 import BeautifulSoup

# The Url I would like to use

URL = "https://worldpopulationreview.com/country-rankings/nobel-prizes-by-country"

# Requesting the HTML and extracting the content

html = requests.get(URL)
soup = BeautifulSoup(html.content, "html.parser")

# Extracting all the data I want

data = soup.find_all("td")
data_list = [i.text for i in data]
data_list

# It has given me a list with each country, the number of nobel prize winners and their population
# I need to extract these into a usable context

# Getting the list of countries first (getting the first results and then each third result)

country_list = data_list[::3]

# Getting the Nobel Prize data

prize_list = data_list [1::3]

# Getting the population data

population_list = data_list[2::3]

# I now have the data I want concerning Nobel prize winners, I can make it into a dataframe and keep only the top 30 results

df1 = pd.DataFrame(country_list)
df2 = pd.DataFrame(prize_list)
df3 = pd.DataFrame(population_list)

# Merging the data

df4 = pd.concat([df1, df2, df3], axis=1)

# Naming my Columns

df4.columns=["Country", "Nobel Prize Winners", "Population"]

# Changing numerical values from strings to integers so that I can perform mathematical operations on them

df4["Nobel Prize Winners"] = df4["Nobel Prize Winners"].astype(int)

# In order to change the following column to integers, I need to remove the commas

df4["Population"] = df4["Population"].str.replace(",", "")
df4["Population"] = df4["Population"].astype(int)

# Making a new columns for "Nobel Prize Winners per Capita"

df4["Nobel Prize Winners Per Capita"] = df4["Nobel Prize Winners"] / df4["Population"]

# Keeping only the first 30 rows of my dataframe

df4 = df4.head(30)

# I now only need income gini data
# For this I will get the relevant data from the world bank
# To do this in the most automated way possible, I will use the relevant Python module

import world_bank_data as wb

# Unfortunately the world bank has this data availible at different years for different countries
# The vast majority of countries have data for 2016
# I will therfore look at the GINI data then and see how good a predictor it is for current "Nobel Prize Winner Per Capita" score
# I will also remove the few countries with missing values, I will still have 25 observations to use

gini = wb.get_series('SI.POV.GINI', date='2016', id_or_value='id', country=["USA", "GBR", "DEU", "FRA", "SWE", "RUS", "JPN", "CHE", "CAN", "AUT", "NLD", "ITA", "POL", "NOR", "DNK", "HUN", "ISR", "AUS", "IRL", "BEL", "ZAF", "IND", "ESP", "CHN", "CZE", "UKR", "FIN", "ARG", "ROM", "EGY"], simplify_index=True)


# Giving my new column a names

# Removing all rows with missing values
country_list = ["USA", "GBR", "DEU", "FRA", "SWE", "RUS", "JPN", "CHE", "CAN", "AUT", "NLD", "ITA", "POL", "NOR", "DNK", "HUN", "ISR", "AUS", "IRL", "BEL", "ZAF", "IND", "ESP", "CHN", "CZE", "UKR", "FIN", "ARG", "ROM", "EGY"]

df4["World Bank Country Code"] = country_list

# Despite putting the countries in the order which I wanted results, my results were returned in alphabetical order
# This meant that I would not be able to match them to their relevant values in the original dataframe
# To get round this, I will use a for loop to search for each result individually and create a list in the order I want
# I can then add this list to the dataframe, as it will be in the right order

empty = []
for i in country_list:
    i = wb.get_series('SI.POV.GINI', date='2016', id_or_value='id', country=i, simplify_index=True)
    empty.append(i)

df4["Gini Income Score"] = empty

# I now have the dataframe with all  the results in the right order
# I now want to get rid of the 5 results with missing values

df4 = df4.dropna()
df4["Gini Income Score"] = df4["Gini Income Score"].values

# I now have fully clean data that I want to use, time to save

df4.to_csv("NobelPrizeData.csv")
