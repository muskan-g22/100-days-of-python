#Create a recursive function to find the sum of digits of a number.
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))