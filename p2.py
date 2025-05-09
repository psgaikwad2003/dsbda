import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\psgai\OneDrive\Desktop\dataset\StudentsPerformance.csv")
df
df.isnull()
df.notnull()

ndf=df
ndf.fillna(0)

df["math score"]=df["math score"].fillna(df['math score'].mean())
df["math score"]=df["math score"].fillna(df['math score'].median())
df["math score"]=df["math score"].fillna(df['math score'].std())

df["math score"]=df["math score"].fillna(df['math score'].min())
df["math score"]=df["math score"].fillna(df['math score'].max())

df
ndf.dropna()
ndf.dropna(how='all')
ndf.dropna(axis=1)

col=['math score','reading score','writing score']
df.boxplot(col)

print(np.where(df['math score']>90))
print(np.where(df['reading score']<25))

import matplotlib.pyplot as plt
plt.scatter('math score','reading score')
plt.xlabel("math score")
plt.ylabel("reading score")
plt.show()

from scipy import stats
z=np.abs(stats.zscore(df['math score']))
print(z)
threshold=0.18
sample_outliers=np.where(z<threshold)
sample_outliers

new_df=df['math score'].plot(kind='hist')
df["log_math"]=np.log10(df['math score'])
df['log_math'].plot(kind='hist')
plt.show()
