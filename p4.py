import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("P4.csv")
start_date = "2024-01-03"
end_date = "2024-01-08"
data = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
plt.plot(data["Date"], data["Close"])
plt.title("Alphabet Inc Stock Prices")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.show()