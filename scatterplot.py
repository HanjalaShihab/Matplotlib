import matplotlib.pyplot as plt

plt.scatter([1,2,3], [50,55, 60], color = 'blue', label = 'Class A')
plt.scatter([1,2,3], [45,50,52], color = 'orange', label = 'Class B')

plt.xlabel('Hours studied')
plt.ylabel('Exam Score')
plt.title('Comparison of Two classes')

plt.legend(loc = 'upper left')
plt.grid(True)

plt.ylim(40, 65)

plt.show()