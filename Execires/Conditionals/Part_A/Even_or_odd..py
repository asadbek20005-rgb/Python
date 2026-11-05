number = int(input("Enter number: "))

if number <= 0:
    print("Please enter a positive number")

result = "Even" if number % 2 == 0 else "Odd"
print(result)