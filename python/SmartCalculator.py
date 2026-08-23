# Build a menu-driven calculator that performs Addition, Subtraction, Multiplication, Division, Modulus, Power, and Floor Division until the user chooses to exit.
while True:
    print("Enter z to exit ")
    expr = input("enter expression using +,-,*,/,//,%,** : ")
    if expr=='z':
        break
    print(eval(expr))
    

