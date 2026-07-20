# Find the missing number from a sequence.
n = int(input("Enter the value of n: "))

numbers = list(map(int, input(f"Enter {n-1} numbers separated by space: ").split()))

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Missing number is:", missing)