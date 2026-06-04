# Do while loop is executed at least once irrespective if the condition is True or not
# Next iteration will only work if the condition is true
# do while loop can be emulated using infinite while loop:

# Example 1-
i =0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break

# Example 2-
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break