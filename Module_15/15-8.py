from random import randint
import pygal


class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die1 = Die()
die2 = Die()
die3 = Die()

results = []


for roll_number in range(50000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

max_num = die1.num_sides + die2.num_sides + die3.num_sides
frequencies = []
for value in range(3, max_num + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling 3 D6 5000 times."
hist.x_labels = range(3, max_num+1)
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6 + D6", frequencies)

hist.render_to_file("3_D6_visual.svg")
