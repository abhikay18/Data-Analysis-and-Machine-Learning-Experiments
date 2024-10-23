import pandas as pd
col_list=["id","first","last","gender","Marks","selected"]
df = pd.read_csv("sample2.csv",usecols=col_list)
print(df)
print("End of Listing\n\n\n")

# Let us create duplicate elements in the given dataset
# This is done using the command concate 2 times as given below

df_duplicated = pd.concat([df]*2, ignore_index=True)
print(df_duplicated)

print("Display before duplication\n\n\n\n")

df_duplicates_removed = pd.DataFrame.drop_duplicates(df_duplicated)
print(df_duplicates_removed)

print("Display after duplication\n\n\n\n")
