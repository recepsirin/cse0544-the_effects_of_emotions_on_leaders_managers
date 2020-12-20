from preprocessing import df_all
from scipy.stats import iqr
import statistics

print("Mean Values in the Distribution")
print(df_all.mean())

print("Median Values in the Distribution")
print(df_all.median())

print("The standard deviation of Intelligent", statistics.stdev(df_all['Intelligent']))
print("The standard deviation of Frustrated", statistics.stdev(df_all['Frustrated']))
print("The standard deviation of Angry", statistics.stdev(df_all['Angry']))
print("The standard deviation of Confident", statistics.stdev(df_all['Confident']))

print("The variance of Intelligent", statistics.variance(df_all['Intelligent']))
print("The variance of Frustrated", statistics.variance(df_all['Frustrated']))
print("The variance of Angry", statistics.variance(df_all['Angry']))
print("The variance of Confident", statistics.variance(df_all['Confident']))

# Descriptive statistics include those that
# summarize the central tendency, dispersion and shape of a dataset’s distribution,
print("Descriptive Statistics", df_all.describe())

# Correlation
print("Correlation between Intelligence and anger", df_all[['Intelligent', 'Angry']].corr())
print("Correlation between Confident and Age", df_all[['Confident', 'Age']].corr())
print("Correlation between Intelligent and Age", df_all[['Intelligent', 'Age']].corr())

# Skewness
"""
Interpreting skewness
1)Highly skewed distribution: If the skewness value is less than −1 or greater than +1.
2)Moderately skewed distribution: If the skewness value is between −1 and −½ or between +½ and +1.
3)Approximately symmetric distribution: If the skewness value is between −½ and +½.
"""
print("___________Skewness___________")
print(df_all.skew())

# IQR
"""
IQR is a measure of statistical dispersion, and is calculated as the difference
between the upper quartile (75th percentile) and the lower quartile (25th percentile).
"""
print("___________Interquartile Range___________")
print(iqr(df_all))

# All Standard Deviation
print("___Standard Deviation along the whole dataset___")
print(df_all.std())
