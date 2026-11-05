age = int(input("Age: "))

if age <= 0:
    print("age must be positive")

if age >= 18:
    print("You may enter")
else:
    print(f"Wait {18-age} more years")

