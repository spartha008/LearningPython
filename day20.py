# Functions
# A function is a block of code that performs a specific task whenever it is called.
# i) Built-in Functions ii) User-defined Functions
# i) These functions are pre-defined and pre-coded in python; e.g.;
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.,


def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass

a = 9
b = 8
# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)

c = 8
d = 75
# gmean2 = (c*d)/(c+d)
# print(gmean2)
# if(c>d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
isGreater(c, d)
calculateGmean(c, d)