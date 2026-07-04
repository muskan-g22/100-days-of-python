#Create a recursive function to calculate power (a^b).
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print("Result:", power(base, exponent))