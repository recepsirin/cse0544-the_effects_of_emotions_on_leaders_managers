from scipy.stats import ttest_ind, ttest_rel
import pandas as pd
from sklearn.preprocessing import LabelEncoder

dataSet = pd.read_csv("./dataset.csv")
le = LabelEncoder()

dataSet['Gender'] = le.fit_transform(dataSet['Gender'])
dataSet['Title'] = le.fit_transform(dataSet['Title'])
dataSet['Manager Level'] = le.fit_transform(dataSet['Manager Level'])
dataSet['Ashamed'] = le.fit_transform(dataSet['Ashamed'])

# Independent two samples t-test
print("Independent two samples t-test")
print(ttest_ind(dataSet['Gender'], dataSet['Title']))
print(ttest_ind(dataSet['Gender'], dataSet['Manager Level']))
print(ttest_ind(dataSet['Gender'], dataSet['Ashamed']))

print(ttest_rel(dataSet['Gender'], dataSet['Title']))
