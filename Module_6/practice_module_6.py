
print("\n**************************************************")
print("< 6-1 >")

jimmy_info = {'first_name': 'jimmy', 'last_name': 'fang',
              'age': 34, 'city': 'beijing'}
print(jimmy_info)


print("\n**************************************************")
print("< 6-2 >")

favorite_number = {'jimmy': 9, 'zicky': 6,
                   'xue_wei': 8, 'mom': 10}
print(favorite_number['jimmy'])
print(favorite_number['zicky'])
print(favorite_number['xue_wei'])
print(favorite_number['mom'])


print("\n**************************************************")
print("< 6-3 >")

dic_01 = {'print': 'print output value on screen',
          'exit': 'logout', 'remove': 'remove the data'}

for name, explain in dic_01.items():
    print(name.title() + ": " + explain.title())


print("\n**************************************************")
print("< 6-4 >")

dic_01 = {'print': 'print output value on screen',
          'exit': 'logout', 'remove': 'remove the data'}

for name, explain in dic_01.items():
    print(name.title() + ": " + explain.title())


x = range(1,11)

for n in x:
    print(n)



