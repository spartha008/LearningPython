# Break statement example-
for i in range(1,101,1):
    print(i, end=" ")
    if(i==50):
        break
    else:
        print("Mississipi")
print("Thank you")

# Continue Statement Example-
for j in [2,3,4,6,8,0]:
    if (j%2!=0):
        continue
    print(j)