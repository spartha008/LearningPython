# Typecasting in Python 
# The conversion of one data type into the other data type is known as type casting in python
# Python supports a wide veriety of functions or methods like: 
# int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc., for the type casting in python

# a = "1"
# # a = 1
# b = "2"
# # b = 2
# print(int(a) + int(b))

# Explicit typecasting - Doing it on will
# Implicit typecasting - Python does it automatically

# Example of explicit typecasting-
string = "15"
number = 7
string_number = int(string) #Throws an error if the string is not a valid integer
sum= number + string_number
print("The sum of both the nummbers is:", sum)

# Example of implicit typecasting-
# a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))