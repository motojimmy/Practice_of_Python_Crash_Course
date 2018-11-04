import pygal
from random import randint

class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die1 = Die()
die2 = Die()

results = []

for roll_number in range(5000):
    result = die1.roll() * die2.roll()
    results.append(result)

print(results)

die1_side_values = list(range(1,die1.num_sides+1))
die2_side_values = list(range(1,die2.num_sides+1))
print(die1_side_values)
print(die2_side_values)

x_lables = []
for die1_side_value in die1_side_values:
    for die2_side_value in die2_side_values:
        final_value = die1_side_value * die2_side_value
        x_lables.append(final_value)
    print(x_lables)


values = list(set(x_lables))
values.sort()
print(values)

frequencies = []
for value in values:
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling 2 D6 and multiply (5000 times)."
hist.x_labels = values
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add("D6*D6", frequencies)

hist.render_to_file("2_D6_Multiply.svg")



