import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats 
from sklearn import preprocessing
df=pd.read_csv(r"C:\Users\psgai\OneDrive\Desktop\dataset\StudentsPerformance.csv")

df

df.mean()
df.types
df.dtypes
df.loc[:,'math score'].mean()
df.mean(axis=1)[0:4]

df.median()
df.loc[:,'reading score'].median()

df.loc[:,'math score'].mode()

df.loc[:,'writing score'].min(skipna=False)

df.loc[:,'writing score'].max(skipna=False)

df.loc[:,'math score'].std()

df.groupby(['math score'])['reading score'].mean()

enc=preprocessing.OneHotEncoder()
enc_df=pd.DataFrame(enc.fit_transform(df[['math score']]).toarray())
enc_df

df_encode=df.join(enc_df)
df_encode
