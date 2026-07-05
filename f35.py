#Create a calculator using functions for +, -, *, /.
def cal(n):
    result=eval(n)
    print(result)

num = input("Enter expression (with operators (+, -, *, /) only) : ")
cal(num)