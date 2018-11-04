from random import randint
class Die():
# 用于模拟掷骰子的类,定义了 骰子面数 和 掷骰子次数
    def __init__(self, sides, times):
        self.sides = sides
        self.times = times

    def roll_die(self):
        time = range(1, self.times + 1)
        for n in time:
            x = randint(1, self.sides)
            print(x)
        print("\n")

shai_zi_01 = Die(6, 10)

shai_zi_01.roll_die()



shai_zi_02 = Die(10, 10)

shai_zi_02.roll_die()


shai_zi_03 = Die(20, 10)

shai_zi_03.roll_die()
