# 84	Create a Bank Account class.
class BankAccount:

    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.balance = balance
        self.history = []

        self.history.append(
            f"Account created with balance: ₹{balance:.2f}"
        )

    # Deposit
    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount

        self.history.append(
            f"Deposited: ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} deposited successfully!")

    # Withdraw
    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount

        self.history.append(
            f"Withdrawn: ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} withdrawn successfully!")

    # Check Balance
    def check_balance(self):

        print(f"Current Balance: ₹{self.balance:.2f}")

    # Transfer Money
    def transfer(self, receiver, amount):

        if receiver == self:
            print("You cannot transfer money to your own account.")
            return

        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount
        receiver.balance += amount

        self.history.append(
            f"Transferred ₹{amount:.2f} to {receiver.account_no}"
        )

        receiver.history.append(
            f"Received ₹{amount:.2f} from {self.account_no}"
        )

        print(
            f"₹{amount:.2f} transferred successfully "
            f"to {receiver.name}."
        )

    # Account Details
    def display_details(self):

        print("\n========== ACCOUNT DETAILS ==========")
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print(f"Balance: ₹{self.balance:.2f}")

    # Transaction History
    def transaction_history(self):

        print("\n========== TRANSACTION HISTORY ==========")

        for i, transaction in enumerate(self.history, start=1):
            print(f"{i}. {transaction}")


# Creating accounts

account1 = BankAccount(
    "1001",
    "Muskan",
    5000
)

account2 = BankAccount(
    "1002",
    "Rahul",
    3000
)


# Menu

while True:

    print("\n==============================")
    print("       BANK ACCOUNT SYSTEM")
    print("==============================")

    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transfer Money")
    print("5. Account Details")
    print("6. Transaction History")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Deposit
    if choice == "1":

        amount = float(
            input("Enter amount to deposit: ")
        )

        account1.deposit(amount)

    # Withdraw
    elif choice == "2":

        amount = float(
            input("Enter amount to withdraw: ")
        )

        account1.withdraw(amount)

    # Balance
    elif choice == "3":

        account1.check_balance()

    # Transfer
    elif choice == "4":

        amount = float(
            input("Enter amount to transfer: ")
        )

        account1.transfer(account2, amount)

    # Account details
    elif choice == "5":

        account1.display_details()

    # Transaction history
    elif choice == "6":

        account1.transaction_history()

    # Exit
    elif choice == "7":

        print("Thank you for using the Bank Account System!")
        break

    else:

        print("Invalid choice!")