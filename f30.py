# Create a function that returns the nth Fibonacci number.
def fib(n):
    a,b=0,1 
    if n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            sum=a+b
            print(sum) 
            a,b=b,sum                        
num=int(input("Enter no. for fibonacci series  : ")) 
fib(num) 