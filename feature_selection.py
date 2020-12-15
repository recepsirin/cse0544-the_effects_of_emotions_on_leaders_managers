from sklearn.feature_selection import SelectKBest, f_classif
import pandas as pd
from preprocessing import df_all

"""
A large number of features can lead to overfitting.Optimizing hyperparameters and training algorithms could take longer.
That is why we want to pick the most relevant features from the beginning.

Univariate Feature Selection: It calculates how strongly  the output feature depends on each feature
from the dataset using statistical tests (like χ2).
Utilizing SelectKBest which has several options when it comes to used statistical tests (the default however is χ2)
"""

df_f_selection = pd.DataFrame()
df_f_selection['Inspired'] = df_all['Inspired']
df_f_selection['Envious'] = df_all['Envious']
df_f_selection['Angry'] = df_all['Angry']

df_age = pd.DataFrame()
df_age['Age'] = df_all['Age']

selector = SelectKBest(f_classif, k=3)

selected_data = selector.fit_transform(df_f_selection, df_age)

print(selected_data)
selected_features = pd.DataFrame(selector.inverse_transform(selected_data), index=df_f_selection.index,
                                 columns=df_f_selection.columns)

selected_columns = selected_features.columns
print(selected_features[selected_columns].head())
