import pandas as pd

df = pd.read_csv("../../dataset/Air_quality_data.csv")

corr = df.corr(numeric_only=True)

print(corr["AQI"].sort_values(ascending=False))