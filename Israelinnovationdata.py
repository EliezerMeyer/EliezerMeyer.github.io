# I will be using Israel as a case study of innovation, since it has an extremely high spend on R&D as a percentage of GDP
# I will first create a bar chart showing this and that the figure has been increasing steadily

# Importing necessary modules, downloading data directly from the World Bank
import world_bank_data as wb
import pandas as pd

# Allowing myself to see the whole dataframe

pd.set_option("display.max_rows", 1000, "display.max_columns", 1000)

# Working on the dataframe

df1 = pd.DataFrame(wb.get_series('GB.XPD.RSDV.GD.ZS', date='1996:2018', id_or_value='id', country="ISR", simplify_index=True))

# Vega Lite is unable to chart the above dataframe so I will try and create a new one based off the values in df1
df2 = pd.DataFrame(df1["GB.XPD.RSDV.GD.ZS"].values)

df2.columns=["Percentage of GDP Spent on R&D"]
df2.insert(1, "Year", range(1996, 1996+len(df2)))

# Saving it to be charted

df2.to_csv("Israeldata.csv")
