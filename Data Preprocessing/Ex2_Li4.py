from numpy import asarray
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

data = asarray([[1,3],[8,5],[6,7],[8,9]])
print("\n Original Data")
print(data)

scaler1 = MinMaxScaler()
scaler2 = StandardScaler()

scaled1 = scaler1.fit_transform(data)
scaled2 = scaler2.fit_transform(data)

print("\n\nThe output of MinMax Scaling")
print(scaled1)


print("\n\nThe output of Standard scaling as z-score")
print(scaled2)
