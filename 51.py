# Rotate a list by k positions (Right Rotation)

arr = [1, 2, 3, 4, 5]
k = 2

# Handle k greater than list length
k = k % len(arr)

# Rotate
rotated = arr[-k:] + arr[:-k]

print("Original List:", arr)
print("Rotated List :", rotated)