am=int(input("enter bill amount :"))
dr=int(input("enter discount in percentage :"))
da=am*(dr/100)
bill=am-da
print("total discount is :",da)
print("bill after discount :",bill)