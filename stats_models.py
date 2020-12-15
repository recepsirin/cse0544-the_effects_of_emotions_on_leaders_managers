import pandas as pd
import statsmodels.formula.api as smf
from preprocessing import df_all

df_smf = pd.DataFrame()

df_smf['Male'] = df_all['Male']
df_smf['Female'] = df_all['Female']
df_smf['Age'] = df_all['Age']
df_smf['Intelligent'] = df_all['Intelligent']
df_smf['Admiring'] = df_all['Admiring']
df_smf['Angry'] = df_all['Angry']
df_smf['Ashamed'] = df_all['Ashamed']

SMF_model_f_i = smf.ols(formula='Female ~ Intelligent', data=df_smf).fit()

print(SMF_model_f_i.summary())

SMF_model_f_a = smf.ols(formula='Female ~ Admiring', data=df_smf).fit()

print(SMF_model_f_a.summary())

SMF_model_f_age = smf.ols(formula='Female ~ Age', data=df_smf).fit()

print(SMF_model_f_age.summary())
