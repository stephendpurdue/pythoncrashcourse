import matplotlib .pyplot as plt


# This creates a line graph showing square numbers from 1 -> 25.

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values] # X squared for each number in x_values

plt.scatter(x_values, y_values, c=y_values, edgecolor='none', s=10) # Plots the list
plt.show() # Initialises the viewer

# Labels

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

# Saving

plt.savefig('squares_plot.png', bbox_inches='tight')