import seaborn as sns
df=sns.load_dataset('iris')
df
df.head()
df.tail()
df.describe()
df.dtypes

import matplotlib.pyplot as plt
axes=plt.subplot(2,2,figsize=(16,9))
sns.histplot(df['sepal_length'])
plt.show()
sns.histplot(df['sepal_width'])
plt.show()
sns.histplot(df['petal_length'])
plt.show()
sns.histplot(df['petal_width'])
plt.show()

axes=plt.subplot(2,2,figsize=(16,9))
sns.boxplot(y='petal_length',x='species',data=df)
plt.show()

sns.boxplot(y='petal_width',x='species',data=df)
plt.show()

sns.boxplot(y='sepal_length',x='species',data=df)
plt.show()

sns.boxplot(y='sepal_width',x='species',data=df)
plt.show()

sns.histplot(data=dataset, x='age', bins=20, color='green', kde=False)
plt.title("Age Distribution with 20 Bins")
plt.show()
