# Övning 4, data structures - list

list1 = []
list2 = []
list3 = []

red = str("red")
green = str("green")
blue = str("blue")
yellow = str("yellow")
purple = str("purple")
pink = str("pink")

#Lägger till i lista .append() för ett värde, .extend([]) för flera värden
list1.extend([red, green, blue])
list2.extend([yellow, purple, pink])
list3.extend([red, yellow])

list5 = list1 + list2

print(list1[0])

print(green in list1)
print(yellow not in list1)

print(list1 + list2)

list4 = (list3*3)
print(list4)

print(list5[0:4])

print(list4.count(red))

print(list4.index(yellow))

print(len(list4))

numbers = []
numbers.extend([2, 3, 5, 7, 11, 13, 17])
print(min(numbers))
print(max(numbers))