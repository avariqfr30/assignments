## Excerise 1 - Number 1 ##
x1 = eval(input("Enter the x-coordinate for point 1 : "))
y1 = eval(input("Enter the y-coordinate for point 1 : "))
x2 = eval(input("Enter the x-coordinate for point 2 : "))
y2 = eval(input("Enter the y-coordinate for point 2 : "))
slope = (y2-y1) / (x2-x1)

print("The slope that connects", (x1, y1), "and", (x2, y2), "is", format(slope, '.5f'))
####

## Exercise 1 - Number 2 ##
v = eval(input("Enter plane take off speed (m/s) : "))
a = eval(input("Enter plane acceleration(m/s^**2): "))
runway = (v**2) / (2*a)

print("The minimum length of the runway needed is", format(runway, '.4f'))
####

## Exercise 1 - Number 4 ##
s = eval(input("Enter side length of hexagon : "))
import math
a = (3 * math.sqrt(3))/(2) * (s**2)

print("The area of a hexagon with side length", s, "is", format(a, '.3f'))
##

## Exercise 1 - Number 3##
subtot = eval(input("Input the subtotal : $"))
tip_perc = eval(input("Input tip (in %) : "))
tip_amount = subtot * (tip_perc/100)
print("Your subtotal is : $", subtot)
print("Your tip is : $", format(subtot * (tip_perc/100), '.2f'))
print("Your total is :$", format((subtot + tip_amount), '.2f'))
##

