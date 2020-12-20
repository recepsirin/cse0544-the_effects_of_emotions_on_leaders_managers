import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from preprocessing import df_all
import numpy as np

df_relationship = df_all[['Confident', 'Proud']]

df_relationship.Confident.corr(df_relationship.Proud, method="pearson")
print(np.corrcoef(df_relationship.Confident, df_relationship.Proud))

# another way to calculate pearson's correlation
corr, p = pearsonr(df_all['Disgusted'], df_all['Age'])
print("correlation -> ", corr, ' p value -> ', p)

sns.scatterplot('Confident', 'Proud', data=df_relationship)
plt.title("The correlation between Confident and Proud")
plt.ylabel('Confident')
plt.xlabel('Proud')
plt.show()
