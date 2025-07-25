import matplotlib.pyplot as plt

product = ['A', 'B', 'C', 'D']
sales = [1000, 1500, 800, 1200]

plt.bar(product, sales, color = 'orange', label = 'Sales 2025')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Product sale comparison')

plt.legend(loc = 'upper right', fontsize = 12)
plt.grid(color = 'grey', linestyle = ':', linewidth = 1)

plt.show()