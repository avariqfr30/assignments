operator = eval(input("Input what to do (1. Addition, 2. Negation, 3. Multiplication, 4. Substraction : "))
num1 = eval(input("Input your 1st number : "))
num2 = eval(input("Input you 2nd number : "))

if operator == 1:
    print("Your result is :", num1 + num2)
elif operator == 2:
    print("Your result is :", num1 - num2)
elif operator == 3:
    print("Your result is :", num1 * num2)
elif operator == 4:
    print("Your result is :", num1 / num2)