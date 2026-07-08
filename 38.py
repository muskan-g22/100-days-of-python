# Check whether two strings are anagrams.
str1 = input("Enter first string: ")
str2 = input("Enter first string: ")
if len(str1)==len(str2):
    freq={}
    freq2={}

    for ch in str1:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in str2:
        if ch in freq2:
            freq2[ch]+=1
        else:
            freq2[ch]=1
    if freq==freq2:
        print("strings are anagram")
    else:
        print("Not anagram")
else:
    print("not anagram")