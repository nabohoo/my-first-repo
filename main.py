from bank import BankAccount

def main():
    account = BankAccount("Alice", 100, 0.05)
    account.deposit(50)
    account.withdraw(30)
    account.add_interest()

    print("\nTransaction History:")
    for record in account.history:
        print(record)

if __name__ == "__main__":
    main()