n=int(input("enter a number : "))   # 6 = its factors are 1,2,3 if 1+2+3=6=enter no. 
a,n1=1,n
sum=0
while a<=n//2:
    if n%a==0:
        sum=sum+a
    a=a+1
print(sum)
if sum==n1:
    print("number is perfect number ")
else:
    print("not a perfect number ")