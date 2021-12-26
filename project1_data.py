# The Global Innovation Index (GII), ranks all countries in terms of innovation and is released every year in a large pdf
# To automate the process of gathering this data, I am creating a program utilising Selenium to automatically take me to the relevent web page to download this pdf
# I then use Tabula to extract the tables directly from the pdf and create Pandas Dataframes

# Importing the necessary Selenium modules

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Setting my chromepath so that Selenium can access Google Chrome

path = "C:\Windows\chromedriver.exe"

driver = webdriver.Chrome(path)

# Telling Python to go to the relevant website to find this years Global Innovation Index Report

driver.get("https://www.wipo.int/global_innovation_index/en/2021/")

# Telling python to click on the link to access this years report, in future years I would just have to change "2021" to the current year

link = driver.find_element(By.LINK_TEXT, "Download the Global Innovation Index 2021")
link.click()

# Python has taken me to the most recent report and I have saved it as "innovation.pdf", it is a 226 page pdf, the data I want is on page 24

# Importing the necessary Tabula and Pandas modules as well as Numpy

import pandas as pd
import tabula
import numpy as np

# Getting python to take the data directly off the tables in the pdf

# I have set "stream=True" since not all columns in the table are separated by lines, but do have white space between them
# Futhermore, Tabula was unable to read the pdf when "lattice=True"

Data = tabula.read_pdf("innovation.pdf", pages="24", stream=True)

# In order for me the see the data better, I went python to show me the complete dataframe

pd.set_option("display.max_rows", 1000, "display.max_columns", 1000)

# The second half of the table is placed next to the first half in the pdf, this means that I have a dataframe with the
# Second half of values in a different column rather than below the rest of the data, I will need to change this

# Changing what I have from a list of lists to a dataframe

df = pd.concat(Data)

# Naming all the columns in the dataframe to help when I split it

df.columns=["A","B","C","D","E","F","G","H","I","J"]

# Constructing my two seprate Dataframes, capturing the two tables on the pdf

df1 = df.loc[:,["A","B","C"]]
df2 = df.loc[:,["F","G","H"]]

# Making df2 have the same heading as df1 so they can be appended more easily

df2 = df2.drop(labels=[0,1])
df2.columns=["A","B","C"]

# Appending the data

df3 = df1.append(df2)

# Giving the columns their correct names, and getting rid of the first two rows that were in the PDF

df3.columns=["GII Rank","Country","GII Score"]
df3 = df3.drop(labels=[0,1])

# I now have a list of 132 countries, showing their GII ranks and scores

# Now time to add inequality data

# I will be using the Wealth gini index, from the World Population Review Website
# In order to be able to update my data with minimal effort if the website updates its figures, I will be scraping the Website

# Importing necessary modules for web scrape

import requests
from bs4 import BeautifulSoup

# Website I want to scrape

URL = "https://worldpopulationreview.com/country-rankings/wealth-inequality-by-country"
html = requests.get(URL)
soup = BeautifulSoup(html.content,'html.parser')

# Using the identifier I have found for results in the table

Results = soup.find_all("td")

# Extracting the text

Results_list = [i.text for i in Results]

# My list shows each country, its wealth Gini index score, and its population
# I will extract only the country names and the wealth Gini scores and make them into two columns in a dataframe

# Extracting the variables I want

Country_list = Results_list[::3]
Gini_list = Results_list[1::3]

# Making the dataframes

dfg1 = pd.DataFrame(Country_list)
dfg2 = pd.DataFrame(Gini_list)

# Merging the dataframes

dfg3 = pd.concat([dfg1,dfg2], axis=1)

# Naming Columns

dfg3.columns=["Country", "Gini Wealth Index Score"]

# In order to merge df3 and dfg3, I need to make sure that country names match
# I have identified that some countries do not exist in both datasets and thus will not be used
# Some countries exist in both dataframes but have different names or spelling, I will make them match
# I will match in preference of df3, since I might want to add more data from the pdf

dfg3["Country"] = dfg3["Country"].replace(["United States", "South Korea", "Hong Kong", "Vietnam", "Russia", "Iran", "Moldova", "Bosnia And Herzegovina", "Brunei", "Tanzania","Dominica", "Trinidad And Tobago", "Bolivia", "Laos"],["United States of America", "Republic of Korea", "Hong Kong, China", "Viet Nam", "Russian Federation", "Iran (Islamic Republic of)", "Republic of Moldova", "Bosnia and Herzegovina", "Brunei Darussalam", "United Republic of Tanzania", "Dominican Republic", "Trinidad and Tobago", "Bolivia (Plurinational State of)", "Lao People’s Democratic Republic"])

# Now that the non-missing values are matching, I can merge the two dataframes based on country

df4 = pd.merge(df3, dfg3, on="Country")

# My dataframe (df4) now shows: GII Rank, Country, GII Score, Gini Wealth Index Score for 126 countries

# It might add more to the analysis to classify countries into income groups, this is done on page 25 of the innovation PDF

# Extracting the income data

Income = tabula.read_pdf("innovation.pdf", pages="25", stream=True)

# Changing what I have from a list of lists to a dataframe

Incomedf = pd.concat(Income)

# The data has been extracted such that column titles are what the first row should be, I will therefore change this

# Here I create a new row based of the column titles and also adjust the indexing of the dataframe
Incomedf.loc[-1] = Incomedf.columns
Incomedf.index = Incomedf.index+1
Incomedf = Incomedf.sort_index()

# Creating new column titles for the DataFrame

Incomedf.columns = ["A", "B", "C", "D", "E"]

# The high-income group is represented by "B", the Upper-Middle income group by "C", the Lower-Middle income group by "D" and the low-income group by "E"

# There are duplicate results in this dataframe (perhaps from an error when I created it), I will therefore remove all duplicates

Incomedf = Incomedf.drop_duplicates(subset=None, keep="first", inplace=False)

# I want to assign each country a score based on its income groups. I will put each group into a dataframe, add a new column with an income score and merge them all back into a new DataFrame
# With an income score of "1" being assigned to the lowest-income group, and an income score of "4" being assigned to the highest income group
# Since some columns were longer than others in the pdf, a lot of the dataframes will have rows full of missing values, I will remove those too

dfib = pd.DataFrame(Incomedf["B"])
dfib["S"] = np.nan
dfib["S"] = dfib["S"].fillna(4)
dfib.columns = ["A", "B"]

dfic = pd.DataFrame(Incomedf["C"])
dfic = dfic.dropna(how = "all")
dfic["S"] = np.nan
dfic["S"] = dfic["S"].fillna(3)
dfic.columns = ["A", "B"]

dfid = pd.DataFrame(Incomedf["D"])
dfid = dfid.dropna(how = "all")
dfid["S"] = np.nan
dfid["S"] = dfid["S"].fillna(2)
dfid.columns = ["A", "B"]

dfie = pd.DataFrame(Incomedf["E"])
dfie = dfie.dropna(how = "all")
dfie["S"] = np.nan
dfie["S"] = dfie["S"].fillna(1)
dfie.columns = ["A", "B"]

# Whilst the above tasks, could be done quicker with a for loop, I was unable to create a dynamic variable

dfis = dfib.append([dfic, dfid, dfie])

dfis.columns=["Country", "Income Score"]

# I now have my dataframe with all countries and their income scores. I can now merge it with the large datadrame

df5 = pd.merge(df4, dfis, on="Country")
print(df5)

# My dataframe now contains: GII Rank, Country, GII Score, Gini Wealth Index Score and Income score for 125 countries
# This script will require very few changes to update all its data, once a new pdf is released and the World Population Review website is updated
# I can now save this data to a csv to be used for making charts on Vega Lite

df5.to_csv("Project_InnovationIndex_WealthInequality_Data.csv")

# I cannot display this data for all countries on a graph as it would overload the reader
# I will therfore select countries who's GII scores, outperform their peers, are in line with their peers, are outperformed by their peers. With peers being countries with the same income scores
# High income countries: Switzerland, Slovenia, Trinidad and Tobego
# Upper middle income countries: China, Colombia, Botswana
# Lower middle income countries: Viet Nam, Senegal, Angola
# Low income countries: Rwanda, Mozambique, Yemen
