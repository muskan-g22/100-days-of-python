# Create a function to find the largest among three numbers.
def largest(a,b,c):
    if(a>b & a>c):
        print(a," is largest")
    elif(b>c & b>a):
        print(b," is largest")
    elif(c>b & c>a):
        print(c," is largest")
    elif(a==b & a>c):
        print(a," is largest")
    elif(a==b & a<c):
        print(c," is largest")
    elif(c==b & c>a):
        print(c," is largest")
    elif(c==b & c<a):
        print(a," is largest")
    elif(a==c & a>b):
        print(a," is largest")
    elif(a==c & a<b):
        print(b," is largest")
    elif(a==b==c):
        print(b," is largest")
    return
num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))
num3=int(input("Enter 3rd number : "))
largest(num1,num2,num3)