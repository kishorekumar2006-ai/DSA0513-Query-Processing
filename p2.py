import pandas as pd
df = pd.read_csv("P2.csv")
count = df["EMPLOYEE_ID"].value_counts()
for emp_id in count.index:
    if count[emp_id] >= 2:
        print(emp_id)