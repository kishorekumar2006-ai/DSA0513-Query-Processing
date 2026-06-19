import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("P5.csv")
start_date = "2024-01-03"
end_date = "2024-01-08"
data = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
plt.bar(data["Date"], data["Volume"])
plt.title("Alphabet Inc Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()