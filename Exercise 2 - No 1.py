## Exercise 2 - No 1 ##
m = eval(input("Enter mass of the cart (kg) : "))
g = 9.8
F = eval(input("Enter the force needed to push cart (N) : "))
a = F/(m*g)
import math
print ("The angle of the ramp is", format(math.degrees(a), '.1f'),"degrees")
####