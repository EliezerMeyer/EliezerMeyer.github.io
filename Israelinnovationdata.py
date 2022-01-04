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

df2.columns=["Israel"]
df2.insert(1, "Year", range(1996, 1996+len(df2)))

# After originally making the chart, I though it would look better with other countries for reference
# I will therefore add data from the UK and US and make a stacked bar chart
# Due to my original data issues, I will call their data and add the values to the original Dataframe

# US

df3 = pd.DataFrame(wb.get_series('GB.XPD.RSDV.GD.ZS', date='1996:2018', id_or_value='id', country="US", simplify_index=True))
df2.insert(2, "United States", pd.DataFrame(df3["GB.XPD.RSDV.GD.ZS"].values))

#UK

df4 = pd.DataFrame(wb.get_series('GB.XPD.RSDV.GD.ZS', date='1996:2018', id_or_value='id', country="GBR", simplify_index=True))
df2.insert(3, "United Kingdom", pd.DataFrame(df4["GB.XPD.RSDV.GD.ZS"].values))


# Saving it to be charted

df2.to_csv("Israeldata.csv")
