## Exercise 2 - No 2 ##
e1 = eval(input("Insert length of edge 1 : "))
e2 = eval(input("Insert length of edge 2 : "))
e3 = eval(input("Insert length of edge 3 : "))

if e1 + e2 > e3 and e1 + e3 > e2 and e2 + e3 > e1:
    print("The perimiter is : ", e1 + e2 + e3)
else : print ("The triangle can not be calculated")
####