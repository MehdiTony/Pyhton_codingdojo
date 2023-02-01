class BankAccount:
    # 1% interest rate and there is the starting account balance
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    # this makes the user being able to deposite in his account balance
    def deposit(self, amount):
        self.balance += amount
    # this makes the user being able to withdraw an amount money from his account
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
    # if the user doesn't have enough money in his account and still wants to withdraw there will be a 5$ fee
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
    #this makes the user be able to see his account and how much his has
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
    #this is the 1% interest rate 
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
    

account = BankAccount(0.01, 1000)

account.deposit(500000)

account.withdraw(1000)

account.display_account_info()

