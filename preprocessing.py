from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd

dataSet = pd.read_csv("./dataset.csv")

ohe = OneHotEncoder(categories='auto')
le = LabelEncoder()

behavioural_features = ["Confident", "Capable", "Efficient", "Intelligent", "Friendly", "Trustworthy", "Warm",
                        "Sincere", "Jealous", "Envious", "Admiring", "Proud", "Inspired", "Angry",
                        "Disgusted", "Hateful", "Frustrated", "Ashamed", "Pity", "Sympathy"]


def apply_label_encoder(column: str):
    """it should ideally be used for response variables"""
    dataSet[column] = le.fit_transform(dataSet[column])


for i in behavioural_features:
    apply_label_encoder(i)

manager_level = dataSet['Manager Level'].values
manager_level = ohe.fit_transform(manager_level.reshape(-1, 1)).toarray()
dataSet = dataSet.drop("Manager Level", axis=1)

df_manager_level = pd.DataFrame(data=manager_level, columns=['Low', 'Middle', 'High'])

gender = dataSet['Gender'].values
gender = ohe.fit_transform(gender.reshape(-1, 1)).toarray()
dataSet = dataSet.drop("Gender", axis=1)

df_gender = pd.DataFrame(data=gender, columns=['Male', 'Female'])

degree = dataSet['Education Degree'].values
degree = ohe.fit_transform(degree.reshape(-1, 1)).toarray()
dataSet = dataSet.drop("Education Degree", axis=1)

df_degree = pd.DataFrame(data=degree, columns=['Bachelor', 'Master', 'MBA', 'PhD'])

title = dataSet['Title'].values
title = ohe.fit_transform(title.reshape(-1, 1)).toarray()
dataSet = dataSet.drop("Title", axis=1)

df_title = pd.DataFrame(data=title, columns=['President', 'Vice-president', 'C-Level', 'Organizational Manager',
                                             'Assistant Manager', 'Supervisor', 'Board Member'])

df_all = pd.concat([df_gender, df_manager_level, df_title, df_degree, dataSet], axis=1)

print(df_all)
# df_all.to_csv('./out.csv')
