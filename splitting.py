# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
from preprocessing import df_all

x = df_all.iloc[:, 17:].values  # independent variable
y = df_all['Age'].values  # dependent variable

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)
