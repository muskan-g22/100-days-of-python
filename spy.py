sum,multi=0,1   #if sum of no=multi of num=spy no.
n=int(input("enter a number of n digits  :"))
while n!=0:
    r=n%10
    sum=sum+r
    multi=multi*r
    n=n//10
if sum == multi:
    print("number is a spy number")
else:
    print("not a spy number")