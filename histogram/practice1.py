import matplotlib.pyplot as plt

scores = [45,67,89,56,78,88,92,60,56,86,33,77,88,90,45,80]

plt.hist(scores, bins=5, color='orange', edgecolor = 'black')

plt.xlabel('Score Range')
plt.ylabel('Number of students')

plt.show()