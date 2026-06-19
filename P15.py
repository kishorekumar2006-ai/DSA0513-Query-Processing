import pandas as pd
df = pd.read_csv("P15.csv")
print(df[df.isnull().sum(axis=1) >= 2])