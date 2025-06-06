import pandas as pd 
import numpy as np 

df = pd.read_excel("Banking_Call_Data.xlsx")

df.replace("unknown", np.nan, inplace=True)

df.dropna(inplace=True)

df.drop_duplicates(inplace=True)


print(df.shape)
print(df.columns)
print(df.head())

