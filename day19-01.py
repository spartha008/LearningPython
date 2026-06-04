# Break and continue 
# Break statement enables a program to skip over a part of code. A break terminates the very loop iy lies within
for i in range(12):
    if(i == 10):
        break
    print("5 X", i+1, "=", 5 * (i+1))

print("Loop ko chodkar nikal gya")

# Continue statement skips the rest of the loop statements and causes the next iteration to occur
for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)