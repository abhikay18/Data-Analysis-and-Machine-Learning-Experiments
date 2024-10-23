import pandas as pd
from matplotlib import pyplot as plt

col_list = ['id', 'name', 'gender', 'physics', 'chemistry', 'maths', 'biology', 'language', 'selected']
df = pd.read_csv('sample3.csv', usecols=col_list)
print(df)
# Create a histogram for physics marks

marks1 = df['physics'].values.tolist()
marks_scored = df['physics'].hist()
plt.title('Histogram for Physics Marks')
plt.xlabel('Physics Marks')
plt.ylabel('Frequency of Physics Marks')
plt.show()

# Create a scatter plot for Physics Vs Chemistry marks
chemistry1 = df['chemistry'].values.tolist()
print(chemistry1)

plt.scatter(chemistry1, marks1, alpha=0.5)
plt.title('Scatter plot chemistry vs physics')
plt.xlabel('Chemistry')
plt.ylabel('Physics')
plt.show()

# Create a Box plot
df.plot.box(title="Box and whisker plot of Marks", grid=False);
plt.show(block=True);

# Create a pie chart for selected based on Gender

sums = df.selected.groupby(df.gender).sum()
plt.pie(sums, labels=sums.index);
plt.show()

# Multiplots
# Box Plot for the dataset

df.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
plt.show()

# Multiplot
# drop columns id,name,gender,selected

cols = df[['id', 'name', 'gender', 'selected']]
df2 = df.drop(cols, axis=1)
pd.plotting.scatter_matrix(df2, alpha=0.2)
plt.show()
