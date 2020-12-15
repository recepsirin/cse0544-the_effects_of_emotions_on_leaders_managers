from sklearn.preprocessing import StandardScaler
from splitting import x_test, x_train

# Scaling
sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)
