n=int(input("enter a number : "))          # eg 9^2=81 , 8+1= 9 = enter no = neon number 
n1=n 
s=n*n
sum=0
while s>0:
    r=s%10
    sum=sum+r
    s=s//10
if sum==n1:
    print("it is a neon number")
else:
    print("not a neven number ")