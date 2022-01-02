// The World Inequality database allows data to be automatically downloaded through Stata. Therefore, for this part of the project to be done in the most automated way, I will use Stata to download the data, and Python within Stata to clean the data and run my analysis

// Setting up my Stata

clear

set more off

cd "C:\Users\meyer\github\EliezerMeyer.github.io\Stata"

//log using "IncomeInequality_WID.log", replace

// Time to get my WID data

// No longer necessary in code, but I originally had to put "ssc install wid"

// I will download both datasets I want, clean them a bit and will then switch to using Python to merge them

// Data for the pre-tax national income share of the bottom 50% of earners in the US

wid, indicators(sptinc) areas(US) perc(p0p50) ages(992) pop(j) clear

drop country variable percentile age pop

rename value IncomeShareBottom50

save "IncomeDataBottom50.dta", replace

// Data for the pre-tax national income share of the top 10% of earners in the US

wid, indicators(sptinc) areas(US) perc(p90p100) ages(992) pop(j) clear

drop country variable percentile age pop

rename value IncomeShareTop10

save "IncomeDataTop10.dta", replace

// Done the Stata work, now for Python

python

import pandas as pd

import numpy as np

# Changing settings so I can see the entire dataframe

pd.set_option("display.max_rows", 1000, "display.max_columns", 1000)

df1 = pd.read_stata(r"C:\Users\meyer\github\EliezerMeyer.github.io\Stata\IncomeDataBottom50.dta")

df2 = pd.read_stata(r"C:\Users\meyer\github\EliezerMeyer.github.io\Stata\IncomeDataTop10.dta")

df3= pd.merge(df1, df2, on="year")

# I now have the data I want
# My next task is to create a chart highlighting the disparity between the income share of the top 10% vs that of the bottom 50%
# I don't want to overload the reader of the chart and will therfore only use data from 2000 for the chart
# I will further not use the years of the pandemic as this may distort the effect we are seeing


df4 = df3.iloc[87:107, :]

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# When plotting, matplotlib is giving the years a weird scale e.g. putting "2002.5" on axis, I will therfore try to change the year values to strings

df4["year"] = df4["year"].values.astype(str)

# Time to plot

plt.plot(df4.loc[:,"IncomeShareBottom50"], df4.loc[:,"year"], label="Bottom 50%", linestyle="", marker="|", markeredgewidth=2)
plt.plot(df4.loc[:,"IncomeShareTop10"], df4.loc[:,"year"], label="Top 10%", linestyle="", marker="|", markeredgewidth=2)
plt.hlines(df4.loc[:,"year"], df4.loc[:,"IncomeShareBottom50"], df4.loc[:,"IncomeShareTop10"])
plt.legend(bbox_to_anchor=(1, 1), title="Income Percentile", numpoints=1)
plt.xlabel("Share of pre-tax national income")
plt.ylabel("Year")
plt.title("The Vast Income Gap in the USA")
plt.savefig(r"C:\Users\meyer\github\EliezerMeyer.github.io\project_pic3.png", bbox_inches="tight")
plt.show()

end




