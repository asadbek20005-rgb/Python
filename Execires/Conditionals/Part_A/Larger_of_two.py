first_num = int(input("First number: "))
second_num = int(input("Second number: "))

if first_num > second_num:
    print(f"Larger: {first_num}")
elif first_num < second_num:
    print(f"Larger: {second_num}")
else:
    print("The numbers are equal")