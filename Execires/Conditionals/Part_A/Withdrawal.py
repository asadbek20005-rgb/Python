balance = 500000

amount = int(input("Enter your amount: "))

if amount <= 0:
    print("Amount must be positive")
elif amount > balance:
    print("Not enough money")
