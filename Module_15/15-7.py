import pygal
from random import randint

class Die:

    def __init__(self, num_sides=8):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die1 = Die()
die2 = Die()
results = []

for roll_number in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)
max_result = die1.num_sides + die2.num_sides
frequencies = []
for result in range(2, max_result+1):
    frequency = results.count(result)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling me D8 1000 times."
hist.x_labels = range(2, max_result+1)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

print(type(hist.x_labels))
hist.add("D8+D8", frequencies)

hist.render_to_file('dice1_visual.svg')
