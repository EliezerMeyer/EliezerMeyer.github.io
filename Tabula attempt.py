import pandas as pd
import tabula
import numpy as np

Data = tabula.read_pdf("innovation.pdf", pages="24", stream=True)

pd.set_option("display.max_rows", 1000, "display.max_columns", 1000)

df = pd.concat(Data)

df.columns=["A","B","C","D","E","F","G","H","I","J"]

df1 = df.loc[:,["A","B","C"]]
df2 = df.loc[:,["F","G","H"]]



df2 = df2.drop(labels=[0,1])
df2.columns=["A","B","C"]

df3 = df1.append(df2)

df3.columns=["GII Rank","Country","GII Score"]
df3 = df3.drop(labels=[0,1])

print(df3)
