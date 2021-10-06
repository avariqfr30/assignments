## Exercise 1 - Number 3 ##
subtot = eval(input("Input the subtotal : $"))
tip_perc = eval(input("Input tip (in %) : "))
tip_amount = subtot * (tip_perc/100)
print("Your subtotal is : $", subtot)
print("Your tip is : $", format(subtot * (tip_perc/100), '.2f'))
print("Your total is :$", format((subtot + tip_amount), '.2f'))
####