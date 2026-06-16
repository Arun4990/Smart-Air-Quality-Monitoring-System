import pandas as pd

df = pd.read_csv("../../dataset/Air_quality_data.csv")

print(df.head())

print(df.columns)

print(df.info())