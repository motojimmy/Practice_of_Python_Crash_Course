from collections import OrderedDict

dic_01 = OrderedDict()

dic_01['print'] = 'print output value on screen'
dic_01['exit'] = 'logout'
dic_01['remove']= 'remove the data'

for key, value in dic_01.items():
    print(key + ": " + value)

