a=int(input("enter a : "))
b=int(input("enter b : "))
while b!=0:
    r=a%b
    a=b
    b=r
print(f"HCF of those 2 number is {a}")