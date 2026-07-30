# Find common keys in two dictionary
dict1 = {'name': 'Muskan', 'age': 21, 'city': 'Ambala'}
dict2 = {'age': 22, 'city': 'Chandigarh', 'country': 'India'}

common_keys = dict1.keys() & dict2.keys()

print("Common Keys:", common_keys)

for key in common_keys:
    print(f"{key} -> {dict1[key]} , {dict2[key]}")