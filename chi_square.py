from preprocessing import df_all
from scipy.stats import chisquare

# Use to test for association between categorical variables
chi_sq, p = chisquare(df_all)

# The larger the chi-square value,
# the more the numbers in the table differ from those we would expect if there were no association

print("Chi square", chi_sq)
print("P", p)
