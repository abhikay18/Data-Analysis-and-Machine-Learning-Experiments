import numpy as np
from numpy.linalg import eig

# define a matrix
X = np.array([[3, 6], [4,7]])

print("Orginal Matrx X and its Shape")
print(X)

print("Original matrix Shape")
print("Original Shape:",X.shape)

# calculate the mean of each column
M = np.mean(X.T, axis=1)
print("\nMean matrix")
print(M)


# center columns by subtracting column means
C = X - M
print("\nCentre the matrix")
print(C)

# calculate covariance matrix of centered matrix
V = np.cov(C.T)
print("\nCovariance of the matrix\n")
print(V)

# eigendecomposition of covariance matrix
values, vectors = eig(V)
print('\n Eigen vectors')
print(vectors)

print('\n Eigen values')
print(values)
