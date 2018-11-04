import matplotlib.pyplot as plt

x_values = list(range(1,6000))
y_values = [x**3 for x in x_values]

plt.title("Cubic Chart Red")
plt.xlabel("x-values", fontsize=14)
plt.ylabel("y-values", fontsize=14)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds)

plt.show()