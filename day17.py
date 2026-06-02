# Introduction to loops
# Loops are used to execute a group of statements a certain number of times
# Types of loops: i) for loop ii) while loop

# Iterating over a string:
name = 'Abhishek'
for i in name:
    print(i, end=", ")

# Iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
    
# Range function: uses loop for specific number of times
for k in range(5):
    print(k)
for k in range(5):
    print(k + 1)
for k in range(1, 9):
    print(k)
# for k in range(1, 200001):
#     print(k)
for k in range(1, 12, 3):
    print(k)