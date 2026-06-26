# Create a function that checks whether a number is prime.
def prime(n):
    if n <= 1:
        print("is not prime")
        return
    for i in range(2,n):
        if(n%i==0):
            print("is not prime")
            return
    
    print("is prime")
num=int(input("Enter number "))
prime(num)