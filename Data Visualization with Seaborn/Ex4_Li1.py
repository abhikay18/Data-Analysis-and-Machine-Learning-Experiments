import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# Create a synthetic dataset

data = {'week': [1, 2, 3, 4, 5],
        'sales': [1.2, 1.8, 2.6, 3.2, 3.8],
        'region': ['south', 'south', 'north', 'north', 'north']
        }

df = pd.DataFrame(data)

# Read the preloaded dataset Iris using data frame 1 - df1

df1 = sns.load_dataset('iris')

sns.set(color_codes=True)

### Univariate Plots

# Histogram plot using barplot

print("\nHistogram of week vs Sales\n")
sns.barplot(x="week", y="sales", hue="region", data=df) \
    .set_title('Bar plot for weeks Vs Sales Data')
plt.show()

# Box Plot

print("\nBox Plot of week and sales data\n")
sns.boxplot(data=df)
plt.xlabel("Statistics", size=18)
plt.ylabel("Week and Sales Data", size=18)
plt.show()

# Distplot - Distribution plots

# Display the histogram by making kde flag as falsse
sns.distplot(df1['sepal_width'], kde=False).set_title('Distribution plot for sepal_width')
plt.xlabel("Sepal Width", size=18)
plt.ylabel("Frequency", size=18)
plt.show()

# Display the Distribution plot by making hist flag as false
sns.distplot(df1['sepal_width'], hist=False).set_title('Distribution plot for sepal_width')
plt.xlabel("Sepal Width", size=18)
plt.ylabel("Frequency", size=18)
plt.show()

# Violin Plot

print("\n Violin Plot of week and sales data\n")
sns.violinplot(data=df).set_title('Violin Plot for week and sales data')
plt.xlabel("Statistics", size=18)
plt.ylabel("Region", size=18)
plt.show()

# Count Plot for Iris Data
sns.countplot(x="region", data=df, palette="Blues").set_title('Count plot Based on regions')
plt.xlabel("Statistics", size=18)
plt.ylabel("Region", size=18)
plt.show()

# Strip plot for Iris Data
print('\n Strip plot\n')
sns.stripplot(x="species", y="petal_length", data=df1).set_title('Strip plot for petal length and class')
