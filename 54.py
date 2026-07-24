# Find the maximum occurring element in a list.
numbers = [2, 5, 3, 2, 8, 5, 2, 5, 5, 1]

frequency = {}

# Count frequency of each element
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_element = None
max_count = 0

# Find element with highest frequency
for key, value in frequency.items():
    if value > max_count:
        max_count = value
        max_element = key

print("Maximum occurring element:", max_element)
print("Frequency:", max_count)