import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("iris.csv")

# Select the first 20 rows for analysis
data = df.iloc[1:20]

# Scatter plot
data.plot.scatter(x='sepal.length', y='sepal.width')
plt.title('Sepal Length vs Sepal Width')
plt.show()

# Histogram for the variety
data.hist(column='variety', by='variety')
plt.suptitle('Histogram by Variety')
plt.show()

# Boxplot grouped by variety
data.boxplot(column='sepal.length', by='variety')
plt.suptitle('Boxplot of Sepal Length by Variety')
plt.show()
