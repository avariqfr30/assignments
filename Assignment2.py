totalrows = eval(input("How many rows ? : "))
for row in range (1, totalrows+1):
    for i in range(1, (totalrows-row)+1):
        print(" ", end=' ')
    for j in range(1, row+1):
        print("*", end=' ')
    print()

