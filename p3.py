import pandas as pd
df = pd.read_csv("P3.csv")
print(df.sort_values(by="JOB_TITLE", ascending=False))