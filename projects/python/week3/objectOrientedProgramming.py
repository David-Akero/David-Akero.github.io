##Basic class with Attributes, Methods, and Encapsulation

class BankAccount:
    ##private attribute with initial balance of 0
    def __init__ (self):
        self.__balance = 0

    ##method to deposit money
    def deposit (self, amount):
        self.__balance += amount
    
    ##method to withdraw money
    def withdraw (self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    ##method to get current balance
    def getBalance (self):
        return self.__balance

##creating an instance of BankAccount  
account = BankAccount()

##depositing and withdrawing money with error handling

valid1 = False

while not valid1:
    try:
        depositAmount = float(input("Enter amount to deposit: "))
        account.deposit(depositAmount)
        print("Current balance is:", account.getBalance())
        valid1 = True
    except ValueError:
        print("Error: Invalid input, please enter numeric values.")

valid2 = False

while not valid2:
    try:
        withdrawAmount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdrawAmount)
        print("Current balance is:", account.getBalance())
        valid2 = True
    except ValueError:
        print("Error: Invalid input, please enter numeric values.")
