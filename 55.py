# Implement linear search.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
numbers = [10, 50, 30, 70, 80, 20]
print(linear_search(numbers, 70))  