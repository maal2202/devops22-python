# Övningsuppgift 3, booleans
x = False
y = False
z = False
#1
result1 = x or y or z
print(result1)
#2
result2 = x and y and z
print(result2)
#3
result3 = x and z and y or y and z and x or z and y and x
print(result3)
#4
result4 = x or y or z
print(result4)
#5
result5 = not x and not y and not z
print(result5)
#6
result6 = not x or not y and not z or not x or not y or not z or not y and not x or not x or not y or not y or not x and not z or not x or not z
print(result6)

# 1. Write a expression with Boolean Operations that:
#   1. result in True if any of x, y, z is True
#   2. result in True if all x, y, z is True
#   3. result in False if any of x, y, z is False
#   4. result in False if all of x, y, z is False
#   5. result in False if any of z, y, z is True
#   6. result in False if all of z, y, z is True