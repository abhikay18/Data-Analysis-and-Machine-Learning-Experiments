import numpy as np
from sklearn import decomposition
X = np.array([[2,6],[1,7]])

print("Orginal Matrx X and its Shape")
print(X)
print("Original Shape:",X.shape)
print("Original matrix\n\n")
# Apply Transform for X

pca = decomposition.PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Transformed Matrix and its Shape")
print(X_pca)
print("Transformed Shape:",X_pca.shape)
print("Transformed Matrix\n\n")

# Apply Inverse Transform

print("After Inverse Transform")
X_new=pca.inverse_transform(X_pca)
print(X_new)
print("After Inverse Transform\n\n\n")


# Explain variance
print('Explained variance\n')
print(pca.explained_variance_ratio_)
print('completed\n\n')

print('Singular values')
print(pca.singular_values_)
print('completed\n\n')
