# Find the first non-repeating character in a string.
s = input("Enter String: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for ch in freq:
    if freq[ch]== 1:
        print(ch)
        break
else:
    print("not present ")