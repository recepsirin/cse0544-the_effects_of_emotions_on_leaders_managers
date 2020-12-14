from sklearn.preprocessing import KBinsDiscretizer
import pandas as pd

dataSet = pd.read_csv("./dataset.csv")

age = dataSet['Age'].values

est = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
est.fit(age.reshape(-1, 1))
Xt = est.transform(age.reshape(-1, 1))
print(Xt)
