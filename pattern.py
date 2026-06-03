n=int(input("enter no. of rows :"))
print("pattern : 1")
for i in range(1,n+1,1):
    print("*"*i)

print("pattern : 2")
for i in range(1,n+1,1):
    print(" "*(n-i),"*"*i,sep="")

print("pattern : 3")
for i in range(n,0,-1):
    print("*"*i," "*(n-i))

print("pattern : 4")
for i in range(n,0,-1):
    print(" "*(n-i),"*"*i,sep="")

print("pattern : 5 ")
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end="")
    print()

print("pattern : 6")
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i,end="")
    print()  

print("pattern : 7 ")
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i,end="")
    print()

print("pattern : 8 ")
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()     

print("pattern : 9 ")
for i in range(1,6,1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

print("patter : 10")
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print(j,end="")
    print() 

print("pattern : 11 ")
for i in range(5,0,-1):
    print(" "*(5-i),end="")
    for j in range(1,i+1,1):
        print(j,end="")
    print()

print("pattern : 12")
for i in range(1,6,1):
    print(" "*(5-i),end="")
    for j in range(1,i+1,1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()
for i in range(4,0,-1):
    print(" "*(5-i),end="")
    for j in range(1,i+1,1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()

print("pattern : 13")
for i in range(1,6,1):
    print(" "*(5-i),"*"*(2*i-1),sep="")
for i in range(4,0,-1):
    print(" "*(5-i),"*"*(2*i-1),sep="")