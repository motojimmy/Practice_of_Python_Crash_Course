import matplotlib.pyplot as plt
import pygal
from random import randint

class Die:
    # 表示一个骰子的类

    def __init__(self, num_sides=6):
        # 骰子默认为6面
        self.num_sides = num_sides

    def roll(self):
        # 返回一个位于1和骰子面数之间的随机值
        return randint(1, self.num_sides)

die = Die()
# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist._title = "Results of rolling one D6 1000 times."
hist.x_labels = range(6)
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
