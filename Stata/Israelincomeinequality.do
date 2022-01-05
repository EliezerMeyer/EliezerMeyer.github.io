// I will now be dowloading income inequality data for Israel directly from the World Inequality Database
// In my last chart I showed Israel's high and growing R&D expenditure, here I will try and see if that has benefited different income groups

// Setting up my Stata

clear

set more off

cd "C:\Users\meyer\github\EliezerMeyer.github.io\Stata"

// Gathering the data, I want the income share of the top 1%, top 10% and the bottom 50%

// Since I want to do the same operation to all of the data, I have written a python loop to write my stata code for me
// My loop did not seem to work in Python for Stata but does work when done in another Python environment
// Below I have copied my python output, and will add my other Python notebook to the chart so that you can see my loop code


// Pasting in my Python output

wid, indicators(sptinc) areas(IL) perc(p0p50) ages(992) pop(j) clear
drop country variable percentile age pop
rename value IncomeSharep0p50
save "IsraelIncomeDatap0p50.dta", replace
wid, indicators(sptinc) areas(IL) perc(p90p100) ages(992) pop(j) clear
drop country variable percentile age pop
rename value IncomeSharep90p100
save "IsraelIncomeDatap90p100.dta", replace
wid, indicators(sptinc) areas(IL) perc(p99p100) ages(992) pop(j) clear
drop country variable percentile age pop
rename value IncomeSharep99p100
save "IsraelIncomeDatap99p100.dta", replace

// Now I move to python to combine that data and save it to create a chart

python

import pandas as pd

# Allowing myself to see a whole dataframe

pd.set_option("display.max_rows", 1000, "display.max_columns", 1000)

df1 = pd.read_stata(r"C:\Users\meyer\github\EliezerMeyer.github.io\Stata\IsraelIncomeDatap0p50.dta")

df2 = pd.read_stata(r"C:\Users\meyer\github\EliezerMeyer.github.io\Stata\IsraelIncomeDatap90p100.dta")

df3 = pd.read_stata(r"C:\Users\meyer\github\EliezerMeyer.github.io\Stata\IsraelIncomeDatap99p100.dta")

# Merging the datasets

df4= pd.merge(df1, df2, on="year")
df5 = pd.merge(df4, df3, on="year")

df5.columns=["Year", "IncomeShareBottom50", "IncomeShareTop10", "IncomeShareTop1"]

# This data is only accurate until 2016, so I will remove all later predictions

df5.drop(df5.tail(5).index, inplace=True)

# Now saving

df5.to_csv(r"C:\Users\meyer\github\EliezerMeyer.github.io\Stata\IsraelIncomeData.csv")

end