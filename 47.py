#  Find duplicate elements in a list.

numbers = [1, 2, 3, 2, 4, 5, 1, 1, 6]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(list(duplicates))