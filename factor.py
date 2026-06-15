n=int(input("enter a number "))
a=1
print("its factors are : ")
while a<=n//2:
    if n%a==0:
        print(a)
    a=a+1