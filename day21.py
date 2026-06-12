# Function Arguments and return statement
# four types of arguments that we can provide in a funtion-
# i) Default Arguments ii) Keyword Arguments iii) Variable Length Arguments iv) Required Arguments

# i) We can provide a default value while creating a function; This way the function assumes a default
# value even if a value is not provided in the function call for that argument

# iv)
# def average(a, b): # a, b = required arguments
#     print("The average is: ", (a+b)/2)

# average(4, 6)

# i)
# def average(a=9, b=1):  #9, 1 = default arguments
    # print("The average is: ", (a+b)/2)

# average(1, 5)
# average(5)
# average(b=9)

# ii) We can provide arguments with key=value, this way the interpreter recognizes the arguments by the parameter name;
# Hence, the order in which the arguments are passed does not matter 
# average(b=9,a=21)


# iii) Sometimes we may need to pass more arguments than those defined in actual function; This can be done using variable length arguments
# Two ways to achieve this-
# Arbitary arguments 

# e.g. 
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum/len(numbers))
    # return 7
    return sum / len(numbers) # Return statement is used to return the value of the expression back to the calling function

c = average(5, 6, 7, 1)
print(c)

# Keyword Arbitary Arguments
# e.g. 
# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname="Buchanan", lname="Barnes", fname="James")