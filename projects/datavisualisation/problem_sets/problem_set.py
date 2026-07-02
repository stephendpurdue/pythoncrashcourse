import matplotlib.pyplot as plt

# 15-1
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=10)
plt.show()

plt.title("Cube Numbers", fontsize=22)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('cubes_plot.png', bbox_inches='tight')