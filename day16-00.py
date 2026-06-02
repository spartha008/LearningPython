# Match Case Statements
# A Match statement will compare a given variable's value to different shapes, also reffered to as the pattern
# The main idea is to keep on comparing the variable with all the present pattern until it fits into one
# Match case contains of three main entities: i) The Match keyword ii) One or more case clauses iii) Expression for each case

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")
    
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)