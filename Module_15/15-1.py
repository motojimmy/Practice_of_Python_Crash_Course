import matplotlib.pyplot as plt

x_values = list(range(1,6))
y_values = [x**3 for x in x_values]

plt.plot(x_values, y_values, linewidth=3)

plt.title("Cubic Chart", fontsize=24)
plt.xlabel("x-values", fontsize=14)
plt.ylabel("y-values", fontsize=14)

plt.tick_params(axis='both', size=14)

plt.show()

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]


plt.title("Cubic Chart", fontsize=24)
plt.xlabel("x-values", fontsize=14)
plt.ylabel("y-values", fontsize=14)

plt.tick_params(axis='both', size=14)

plt.scatter(x_values, y_values, c= y_values, cmap=plt.cm.Blues)
plt.show()
