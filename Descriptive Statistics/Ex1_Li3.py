from scipy import stats
data = [1,2,3,4,5,6,8,8,8,8,9,10,10,10,12,14,18,18,18,22,39,44,55,55,55,55,66,78,79,88]

print("\n Details of the data \n", stats.describe(data))
print("\n The cumulative frequency of the data-n",stats.cumfreq(data))
print("\n The Geometric mean of the data-n",stats.gmean(data))
print("\n The Harmonic mean of the data-n",stats.hmean(data))
print("\n The IQR of the data-n",stats.iqr(data))
print("\n The Zscore of the data-n",stats.zscore(data))
print("\n The skewness of the data-n",stats.skew(data))
print("\n The Kurtosos of the data-n",stats.kurtosis(data))

# Check correlation of the data

data = [1,2,3,6,8,10]
data1 = [2,3,4,5,9,12]

print("\n The Spearman correlation of the data-n",stats.spearmanr(data,data1))
