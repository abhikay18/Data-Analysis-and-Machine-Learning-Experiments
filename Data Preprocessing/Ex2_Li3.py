import pandas as pd
df = pd.DataFrame({
                'm1':[50,'A',60,'A',80],
                'm2':[60,'A','60','A',80],
                'm3':[50,70,'A','A',60],
                'm4':[60,'A','A','A',60],
                'm5':['A','A','A',10,20]
                })

df = df.apply(pd.to_numeric,errors='coerce')

print(df)

print('Dataframe with NaN\n\n\n')
# Make all the NaN in Mark5 as zero
df['m5']=df['m5'].fillna(0)
print(df)
print('Making m5 NaN as 0 using fillna() function\n\n\n\n')

df1 = df.copy()
df1['m2'].fillna(df1['m2'].mean(),inplace=True)
print(df1)
print('Making m5 NaN as mean using fillna() function\n\n\n\n')

df2 = df.copy()
df1['m3'].fillna(df1['m2'].median(),inplace=True)
print(df2)
print('Making m5 NaN as median using fillna() function\n\n\n\n')

# Dropping all columns having NaN
df=df.dropna(axis=1)
print(df)
print('Dropping all columns having NaN\n\n\n\n')
