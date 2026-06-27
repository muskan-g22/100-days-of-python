 # Create a function that returns the factorial of a number.
def fact(n):
    
    if n==0:
        print(1)
    else:
        fact1=1
        for i in range(1,n+1):
            fact1=fact1*i
        return fact1
num=int(input("Enter no. to calculate factorial  : "))  
print(fact(num)) 