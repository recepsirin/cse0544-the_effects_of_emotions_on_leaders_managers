# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
from preprocessing import df_all

x = df_all.iloc[:, 1:3].values  # independent variable
y = df_all.iloc[:, 3:].values  # dependent variable

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)
