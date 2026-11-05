age = int(input("Age: "))

if age <= 0:
    print("You can't enter negative numbers")

result = "20.000 sum" if age <= 12 else "40.000 sum"
print(result)

