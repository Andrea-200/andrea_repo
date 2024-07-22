class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

# Example usage:
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")

# Attempting to access the private attribute directly will raise an error
# print(account.__balance)  # This will raise an AttributeError
