import math
from fractions import Fraction

## Inserting the numerator and denominator and GCD ##
num = eval(input("Enter numerator (Must be greater than 0) : "))
while not num > 0:
    print("Numerator must be greater than 0")
    num = eval(input("Re-enter numerator (Must be greater than 0) : "))
denom = eval(input("Emter denominator (Must be greater than 0) : "))
while not denom > 0:
    print("Denominator must be greater than 0")    
    denom = eval(input("Re-enter denominator (Must be greater than 0) : "))
gcd = math.gcd(num,denom)

## If numerator < denominator (Proper Fraction)
if num < denom:
    print(num,"/",denom,"is a Proper Fraction")
else:
    print(num,"/",denom,"is not a Proper Fraction")

## Can the fraction be simplified? ##
if gcd != 1:
    print("The fraction can be reduced to", Fraction(num,denom))
if gcd == 1:
    print("The fraction can not be reduced.")

## If numerator > denominator (Improper Fraction, Mixed Number / Whole Number)
if num > denom:
    a = num // denom
    b = num % denom
    if num % denom != 0:
        print('The mixed number is {} and {}' .format(a, Fraction(b,denom)))
    else:
        print('The whole number is', num//denom)
            


    
    