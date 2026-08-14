# 83	Create an ATM Simulation Program.
accounts = {}


# Create Account
def create_account():
    account_no = input("Enter Account Number: ")

    if account_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Account Holder Name: ")

    pin = input("Create 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    balance = float(input("Enter Initial Deposit: "))

    if balance < 0:
        print("Balance cannot be negative.")
        return

    accounts[account_no] = {
        "name": name,
        "pin": pin,
        "balance": balance,
        "history": []
    }

    accounts[account_no]["history"].append(
        f"Account created with deposit: ₹{balance:.2f}"
    )

    print("Account created successfully!")


# Login
def login():
    account_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if account_no not in accounts:
        print("Account not found!")
        return None

    if accounts[account_no]["pin"] != pin:
        print("Incorrect PIN!")
        return None

    print(f"\nWelcome, {accounts[account_no]['name']}!")

    return account_no


# Check Balance
def check_balance(account_no):
    balance = accounts[account_no]["balance"]

    print(f"Current Balance: ₹{balance:.2f}")


# Deposit Money
def deposit(account_no):
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    accounts[account_no]["balance"] += amount

    accounts[account_no]["history"].append(
        f"Deposited: ₹{amount:.2f}"
    )

    print(f"₹{amount:.2f} deposited successfully!")


# Withdraw Money
def withdraw(account_no):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if amount > accounts[account_no]["balance"]:
        print("Insufficient balance!")
        return

    accounts[account_no]["balance"] -= amount

    accounts[account_no]["history"].append(
        f"Withdrawn: ₹{amount:.2f}"
    )

    print(f"₹{amount:.2f} withdrawn successfully!")


# Transfer Money
def transfer(account_no):
    receiver = input("Enter Receiver Account Number: ")

    if receiver not in accounts:
        print("Receiver account not found!")
        return

    if receiver == account_no:
        print("You cannot transfer money to your own account.")
        return

    amount = float(input("Enter amount to transfer: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if amount > accounts[account_no]["balance"]:
        print("Insufficient balance!")
        return

    accounts[account_no]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    accounts[account_no]["history"].append(
        f"Transferred ₹{amount:.2f} to Account {receiver}"
    )

    accounts[receiver]["history"].append(
        f"Received ₹{amount:.2f} from Account {account_no}"
    )

    print(f"₹{amount:.2f} transferred successfully!")


# Change PIN
def change_pin(account_no):
    old_pin = input("Enter Current PIN: ")

    if old_pin != accounts[account_no]["pin"]:
        print("Incorrect current PIN!")
        return

    new_pin = input("Enter New 4-digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    accounts[account_no]["pin"] = new_pin

    accounts[account_no]["history"].append(
        "PIN changed successfully"
    )

    print("PIN changed successfully!")


# Transaction History
def transaction_history(account_no):
    history = accounts[account_no]["history"]

    print("\n========== TRANSACTION HISTORY ==========")

    if not history:
        print("No transactions found.")
        return

    for i, transaction in enumerate(history, start=1):
        print(f"{i}. {transaction}")


# ATM Menu
def atm_menu(account_no):

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Change PIN")
        print("6. Transaction History")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_no)

        elif choice == "2":
            deposit(account_no)

        elif choice == "3":
            withdraw(account_no)

        elif choice == "4":
            transfer(account_no)

        elif choice == "5":
            change_pin(account_no)

        elif choice == "6":
            transaction_history(account_no)

        elif choice == "7":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")


# Main Program
while True:

    print("\n================================")
    print("       ATM SIMULATION")
    print("================================")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        account_no = login()

        if account_no is not None:
            atm_menu(account_no)

    elif choice == "3":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice!")