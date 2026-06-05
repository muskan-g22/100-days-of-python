n=int(input("enter a number : "))   #eg 306=> 3+0+6=9  if 306%9==0 == neven no.
n1=n
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
if n1%sum==0:
    print("it is neven number ")
else:
    print("not a neven number ")