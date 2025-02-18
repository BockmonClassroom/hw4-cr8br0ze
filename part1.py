import numpy as np
import pandas as pd

#load iris
df = pd.read_csv('Iris.csv')
numbers = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

#normalize
df_normalized = df.copy()
df_normalized[numbers] = (df[numbers] - df[numbers].min()) / (df[numbers].max() - df[numbers].min())

#standardize
df_standardized = df.copy()
df_standardized[numbers] = (df[numbers] - df[numbers].mean()) / df[numbers].std()

#save datasets
df_normalized.to_csv('Iris_normalized.csv')
df_standardized.to_csv('Iris_standardized.csv')
