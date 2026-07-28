# Merge two dictionaries.


#  using update()

dict1 = {}
dict2 = {}

n1 = int(input("Enter number of elements in first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

n2 = int(input("\nEnter number of elements in second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

dict1.update(dict2)

print("\nMerged Dictionary:")
print(dict1)

dict3 = {"a": 10, "b": 20, "c": 30}
dict4 = {"d": 40, "e": 50, "f": 60}

merged_dict = dict3 | dict4

print("Merged Dictionary:")
print(merged_dict)

dict5 = {"a": 10, "b": 20, "c": 30}
dict6 = {"d": 40, "e": 50, "f": 60}

merged_dict0 = {**dict5, **dict6}

print("Merged Dictionary:")
print(merged_dict0)