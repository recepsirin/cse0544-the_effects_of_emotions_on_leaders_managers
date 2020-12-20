from scipy.stats import f_oneway
from preprocessing import df_all
import numpy as np
import matplotlib.pyplot as plt


print(f_oneway(df_all['Intelligent'], df_all['Jealous'], df_all['Trustworthy']))