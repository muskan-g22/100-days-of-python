# Find the second largest number in a list.
def second_largest(numbers):
    large = numbers[0]
    sec_large = numbers[0]
    for n in numbers:
        if n>large:
            sec_large = large
            large = n
        elif n>sec_large and n!=large:
            sec_large=n
    return sec_large

    

numbers = [2, 12, 5, 20, 8, 15]

print(second_largest(numbers))