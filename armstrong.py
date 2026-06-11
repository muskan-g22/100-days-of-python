n=int(input("enter a number : "))
sum,n1=0,n
while n!=0:
    r=n%10
    sum=sum+r**3
    n=n//10
if sum==n1:
    print("armstrong number ")
else:
    print("not armstrong")