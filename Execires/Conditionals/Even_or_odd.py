number = int(input("enter number: "))
if number <= 0:
    print("please enter a positive number")
else:
    result = "Even" if number % 2 == 0 else "Odd"
    print(result)

