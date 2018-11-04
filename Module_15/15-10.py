import matplotlib.pyplot as plt
from random import randint
import pygal

class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die1 = Die()
die2 = Die()

results = []

for roll_num in range(5000):
    result = die1.roll() * die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides * die2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

plt.plot(list(range(1, max_result+1)), frequencies, linewidth=1)
plt.title("Results of rolling 2 D6 and multiply (5000 times)")
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

plt.show()

print("\n################################################")


import pygal
from random_walk import RandomWalk

rw = RandomWalk(1000)
rw.fill_walk()

xy_chart = pygal.XY(stroke=False)  # stroke=False散点不连线
xy_chart.title = 'RandomWalk'
pygal.Line(include_x_axis=False, include_y_axis=False)

# 把生成的值变成坐标
xy_list = []
for (x, y) in zip(rw.x_values, rw.y_values):
    xy_list.append((x, y))

xy_chart.add('data', xy_list)

xy_chart.render_to_file('RandomWalk.svg')
