# Invert a dictionary (swap key-value pairs).
original = {"a": 1, "b": 2, "c": 3}

# Swap key and value
inverted = {value: key for key, value in original.items()}

print(inverted)
# Output: {1: 'a', 2: 'b', 3: 'c'}