import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# Create a synthetic dataset

data = {'week': [1,2,3,4,5],
        'sales':[1.2,1.8,2.6,3.2,3.8],
        'region':['south','south','north','north','north']
       }

df = pd.DataFrame(data)

# Read the preloaded dataset Iris using data frame 1 - df1

df1 = sns.load_dataset('iris')

sns.set(color_codes=True)

### Bivariate Plots

# Joint Plot
print('\n Joint Plot of week and sales\n')
sns.jointplot(x = 'week',y = 'sales',data = df)
plt.show()

#lmplot

print('\n lmplot of week and sales Based on Region\n\n')
g1 = sns.lmplot(x="week", y="sales", hue="region", data=df)

### Multivariate Plots

# pairplot
sns.pairplot(df1,hue = 'species',kind = "scatter")
plt.show()
