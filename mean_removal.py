"""
It involves removing the mean from each feature so that it is centered on zero.
Mean removal helps in removing any bias from the features.
"""
from preprocessing import df_all
from sklearn.preprocessing import scale

scaled_data = scale(df_all)

print(scaled_data.mean(axis=0))
print(scaled_data.std(axis=0))
