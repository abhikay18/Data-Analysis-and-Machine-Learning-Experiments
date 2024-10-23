import pandas as pd
col_list=["id","first","last","gender","Marks","selected"]
df = pd.read_csv("sample1.csv",usecols=col_list)
print(df)
print(df.shape)
print(df.head(5))
print(df.describe())
