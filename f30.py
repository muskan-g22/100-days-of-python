# Create a function that returns the nth Fibonacci number.
def fib(n):
    a,b=0,1
    for i in range(n):
        print(a) 
        a,b=b,a+b                       
num=int(input("Enter no. for fibonacci series  : ")) 
fib(num) 