from sklearn.decomposition import PCA
from scaling import X_test, X_train

pca = PCA()
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

print(X_train)
print(X_test)

# returns the variance caused by each of the principal components.
explained_variance = pca.explained_variance_ratio_

print(explained_variance)
