a=int(input("enter a :"))
b=int(input("enter b :"))
print("value of a=",a,"value of b =",b)
print("value of a=",a)
print("value of b=",b)
#percentile method
print("value of a= %i and b = %i " %(a,b))
print("value of a=(%10i)"%a)
c=float(input("enter c :"))
print("value of d=(%5.2f)"%c)
#format method
print("value of a={} and b={} and c={}".format(a,b,c))
print("value of b={1} and c={2} and a={0}".format(a,b,c))
print("value of c={d2} and b={d1} and a={d0}".format(d0=a,d1=b,d2=c))
print(f"value of b={b} and a={a} and c={c}")         #fast string formatting