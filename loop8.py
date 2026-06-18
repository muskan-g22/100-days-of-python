sum,multi=0,1
n=int(input("enter a number of n digits  :"))
while n!=0:
    r=n%10
    sum=sum+r
    multi=multi*r
    n=n//10
print("sum of digits of number is ",sum)
print("multiplication of digits if number is",multi)