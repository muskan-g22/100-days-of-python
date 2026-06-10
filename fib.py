n=int(input("enter number of series : "))
a,b,i=0,1,3
if n<0:
    print("enter positive term ")
elif n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else: 
    print(a)
    print(b)
    while i<=n:
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1