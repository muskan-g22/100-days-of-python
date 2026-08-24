# Create a program that prints at least six different star and number patterns chosen by the user.

def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def diamond(n):
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def number_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(str(i) for _ in range(i)))

def floyds_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()

def number_triangle(n):
    for i in range(1, n + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))

def display_menu():
    print("\n" + "=" * 35)
    print("      PATTERN GENERATOR MENU      ")
    print("=" * 35)
    print("1. Right-Angled Star Triangle")
    print("2. Star Pyramid")
    print("3. Star Diamond")
    print("4. Repeating Number Pyramid")
    print("5. Floyd's Triangle")
    print("6. Sequential Number Triangle")
    print("7. Exit")
    print("=" * 35)

def main():
    patterns = {
        1: right_triangle,
        2: pyramid,
        3: diamond,
        4: number_pyramid,
        5: floyds_triangle,
        6: number_triangle
    }

    while True:
        display_menu()
        try:
            choice = int(input("Select a pattern (1-7): "))
            if choice == 7:
                print("Exiting Pattern Generator. Happy coding!")
                break
            elif choice in patterns:
                rows = int(input("Enter number of rows/size: "))
                if rows <= 0:
                    print("Please enter a positive integer.")
                    continue
                print("\n--- Output ---")
                patterns[choice](rows)
            else:
                print("Invalid choice! Please choose a number between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()