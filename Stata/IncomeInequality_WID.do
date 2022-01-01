// The World Inequality database allows data to be automatically downloaded through Stata. Therefore, for this part of the project to be done in the most automated way, I will use Stata to download the data, and Python within Stata to clean the data and run my analysis

// Setting up my Stata

clear

set more off

cd "C:\Users\meyer\github\EliezerMeyer.github.io\Stata"

//log using "IncomeInequality_WID.log", replace

// Time to get my WID data

// No longer necessary in code, but I originally had to put "ssc install wid"

wid, indicators(shweal) areas(FR) perc(p90p100 p99p100) ages(992) pop(j) clear


