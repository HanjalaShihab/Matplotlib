import matplotlib.pyplot as plt
import pandas as pd

file_path = "barcharts/spotify.csv"
data = pd.read_csv(file_path, index_col='Date', parse_dates=True)

x = data.index  # Date is the index now
y = data['Shape of You']

plt.bar(x, y, color='red')

plt.show()
