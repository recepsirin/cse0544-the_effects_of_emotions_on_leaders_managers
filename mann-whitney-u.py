from scipy.stats import mannwhitneyu
from preprocessing import df_all
import matplotlib.pyplot as mp

stat, p = mannwhitneyu(df_all['Envious'], df_all['Age'])

print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')
