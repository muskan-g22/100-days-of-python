l=int(input("enter length"))
b=int(input("enter breadth"))
print("press 1 for area \n press 2 for perimeter ")
n=int(input("enter choice :"))
if n==1:
    area=l*b
    print("area of rectangle is :",area)
elif n==2:
    per=2*(l+b)
    print("perimeter of rectangle is :",per)
else:
    print("valid choice")
