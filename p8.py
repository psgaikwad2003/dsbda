import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset=sns.load_dataset('titanic')
dataset

sns.displot(x=dataset['age'],bins=10)
sns.displot(dataset['age'],bins=10,kde=False)
plt.show()

sns.jointplot(x=dataset['age'],y=dataset['fare'],kind='scatter')
plt.show()

sns.jointplot(x=dataset['age'],y=dataset['fare'],kind='hex')
plt.show()

sns.rugplot(dataset['fare'])
plt.show()

sns.barplot(x='sex',y='age',data=dataset)
plt.show()

sns.barplot(x='sex',y='age',data=dataset,estimator=np.std)
plt.show()

sns.countplot(x='sex',data=dataset)
plt.show()

sns.boxplot(x='age',y='sex',data=dataset)
plt.show()

sns.boxenplot(x='sex',y='age',data=dataset,hue="survived")
plt.show()

sns.violinplot(x='sex',y='age',data=dataset)
plt.show()

sns.violinplot(x='sex',y='age',data=dataset,hue="survived")
plt.show()

sns.stripplot(x='sex', y='age', data=dataset, jitter=True)
plt.show()

sns.stripplot(x='sex',y='age',data=dataset,hue="survived")
plt.show()

sns.swarmplot(x='sex',y='age',data=dataset)
plt.show()


