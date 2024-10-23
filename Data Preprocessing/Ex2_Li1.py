import pandas as pd
col_list=["id","first","last","gender","Marks","selected"]
df = pd.read_csv("sample2.csv",usecols=col_list)
print(df)
print("End of Listing\n\n\n")

# Let us convert the in Gender column, make Female as 0 and
# male as 1 using LabelEncoder in scikitlearn method

from sklearn.preprocessing import LabelEncoder
df_gender_encode=LabelEncoder()
df.gender=df_gender_encode.fit_transform(df.gender)
# One can observe that female is coded as 0 and Male as 1
print(df)
print("End of Listing\n\n\n")

# Now one can scale the marks to remove mean

from sklearn import preprocessing
df.Marks = preprocessing.scale(df.Marks)
scaled_df= preprocessing.scale(df.Marks)
print(df)
print("Scaling of marks is completed\n\n\n\n")


newarr = scaled_df.reshape(-1,1)
scaled_df_bin = preprocessing.Binarizer(threshold=0.5).transform(newarr)
df['Marks']=scaled_df_bin
print(df)
print("Binarizarion of marks is completed\n\n\n\n")
