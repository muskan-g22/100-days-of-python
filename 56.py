# implement binary search.
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half
            
    return -1  # Target not found

# Example (Must be sorted)
numbers = [10, 30, 50, 70, 90]
print(binary_search(numbers, 70))  # Output: 3
