import matplotlib.pyplot as plt

x_values = list (range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues,
            edgecolors='none',s=40)
plt.title("Test Chart", fontsize=24)
plt.xlabel("x-axis", fontsize=14)
plt.ylabel("y-axis", fontsize=14)


plt.savefig('data_visualization.png', bbox_inches="tight")




