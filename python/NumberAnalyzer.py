import math

try:
    num = int(input("Enter number: "))
    
    # 1. Positive/Negative/Zero Check
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")
        
    # 2. Even/Odd Check
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
        
    # 3. Prime Check (Fixed Logic)
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break  # Exit loop immediately if a factor is found
                
    if is_prime:
        print("prime")
    else:
        print("not prime")
        
    # 4. Armstrong Check (Fixed for Negative Numbers)
    num_str = str(abs(num))  # Use absolute value to avoid length errors with '-'
    length = len(num_str)
    armstrong_sum = 0
    temp = abs(num)
    
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** length
        temp //= 10
        
    if num >= 0 and num == armstrong_sum:
        print("armstrong number")
    else:
        print("not armstrong number")
        
    # 5. Palindrome Check (Fixed Syntax)
    if str(num) == str(num)[::-1]:
        print("palindrome")
    else:
        print("not palindrome")

except ValueError:
    print("Please enter a valid Number.")
