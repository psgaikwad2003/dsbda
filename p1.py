import pandas as pd
df=pd.read_csv(r"C:\Users\psgai\OneDrive\Desktop\dataset\zomato.csv")
df.head(5)
df.tail(n=10)
df.index
df.columns
df.dtypes
df.fillna("Unknown", inplace=True)
df["rate"]=df["rate"].astype('object')
df.columns.values
df.isnull().sum()
df.describe(include='all')
df['address']
df.sort_index(axis=1,ascending=True)
df.sort_values(by="address")
df.iloc[5]
df[0:3]
df.loc[:,["address","name"]]
df.iloc[:3,:]
df.iloc[:,:3]
df.iloc[:1,:1]
