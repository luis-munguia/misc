# -*- coding: utf-8 -*-

"""
item = "car"
cost = 13499.99

"{:10}{:>10,.{prec}f}".format(item,cost,prec=2)

f"The {item} cost is {cost}"

#Python 3.6 and later introduced F-Strings,
#you can use placeholder {} to evaluate code inside.
#enumerate is better than using range and len in a for loop.

list1 = ["Luis","Eduardo","Javier","Victor","Eduardo"]
for i in range(len(list1)):
    print(list1[i])

friends = ["Pablo", "Rodolfo", "Rafael", "Carlos", "Victor", "Luis"]
list1 = ["Luis", "Carlos"]

common = set(list1) & set(friends)
common

numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        continue
    result += item
print(result)

"""
"""
names = ['Logan', 'Paul', 'George', 'Ringo']

for i in range(len((names))):
    if names[i] == "John":
        print("He's here")
        break
else:
    print("He's not here")
"""
"""
friends = [("Luis","Munguia",32),("Pedro","Munguia",34),("Janeth","Moreno",27),("Mitl","Llamas",None)]

x = 0
y = 0

for i in range(len(friends)):
    if friends[i][2] == None:
        continue
    x = friends[i][2] + x
    y += 1
ave = x / y

for j in range(len(friends)):
    if friends[j][2] == None:
        continue
    print(friends[j][0])
    if friends[j][2] > ave:
        print("Old")
    else:
        print("Young")
"""
