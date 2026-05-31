rev=0
n=int(input("enter a number : "))
n1=n
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
print (f"number is {n1} and its reverse is {rev} thus ..")
if n1==rev:
    print("number is palindrom")
else:
    print("number is not a palindrom")