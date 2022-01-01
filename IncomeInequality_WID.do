// The World Inequality database allows data to be automatically downloaded through Stata. Therefore, for this part of the project to be done in the most automated way, I will use Stata to download the data, and Python within Stata to clean the data and run my analysis

// Setting up my Stata

clear

set more off

cd "C:\Users\meyer\github\EliezerMeyer.github.io"

log using "IncomeInequality_WID.log", replace


