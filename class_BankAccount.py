class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Create an object from the BankAccount class
account = BankAccount(1000)

# Try to access the object's private attribute
try:
    print(account.__balance)
except AttributeError:
    print("Cannot access private attribute.")

# Call the object's methods
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(200)
print(account.get_balance())  # Output: 1300