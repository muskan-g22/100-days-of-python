a=1
s1,s2=0,0
n=int(input("enter end term : "))
while a<=n:
    if a%2==0:
        s1=s1+a
    else:
        s2=s2+a
    a=a+1
print(f"sum of even number from series is {s1} and odd number is {s2}")