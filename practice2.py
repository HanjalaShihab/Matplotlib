import matplotlib.pyplot as plt

x = ['Mon', 'Tues', 'Wed','Thur', 'Fri']
y = [10,15,7,20, 12]

plt.plot(x,y)

plt.title("Bakery sales this week!")

plt.xlabel("Day of the week")
plt.ylabel("Sales per day")

plt.show()