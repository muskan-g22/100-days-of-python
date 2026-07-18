# Merge two lists and remove duplicates.

# Define two sample lists with overlapping elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Merge lists using '+' and remove duplicates by converting to a set
merged_list = list(set(list1 + list2))

print("Merged list without duplicates (unordered):")
print(merged_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
