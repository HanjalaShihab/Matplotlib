import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1000, 1500, 1200, 1800]

plt.plot(months, sales, color = 'red', linestyle= '--', linewidth = 2, marker = 'o', label = '2025 sales data')
plt.title("Monthly sales data report")

plt.xlabel("Months")
plt.ylabel("Sales per month")

plt.show()