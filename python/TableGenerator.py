start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("\n" + "=" * 40)
print(f" Multiplication Tables: {start} to {end}")
print("=" * 40)

for num in range(start, end + 1):
    print(f"\n--- Table of {num} ---")

    for i in range(1, 11):
        print(f"{num:2} × {i:2} = {num * i:3}")

print("\n" + "=" * 40)