# Count frequency of elements using a dictionary.
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
frequency = {}

for item in elements:
    # Fetch existing count (default to 0) and add 1
    frequency[item] = frequency.get(item, 0) + 1

print(frequency)

