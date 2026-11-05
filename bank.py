class BankAccount:
    def __init__(self, owner, balance=0, interest_rate=0.02):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: {amount}")
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew: {amount}")
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.history.append(f"Interest added: {interest}")
        print(f"Added interest {interest}. New balance: {self.balance}")