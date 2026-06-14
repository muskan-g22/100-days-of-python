print("press 1 to check number is even or odd")
print("press 2 to check larger of 2 numbers ")
print("press 3 to check number is buzz or not")
ch=int(input("enter choice"))
if ch==1:
    n=int(input("enter number :"))
    if n%2==0:
        print("number is even")
    else:
        print("number is odd")
elif ch==2:
    a=int(input("enter 1st number :"))
    b=int(input("enter 2nd number :"))
    if a>b:
        print("1st number is greater")
    elif b>a:
        print("2nd number is greater")
    else:
        print("both numbers are equal")
elif ch==3:
    n=int(input("enter number"))
    if n%7==0 or n%10==7:
        print("number id buzz")
    else:
        print("not a buzz number")
else:
    print("enter valid choice...")