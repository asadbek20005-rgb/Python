name = input("Enter name: ")
name = name.replace(" ", "")

if name.isalpha():
    print("Hello " + name)
else:
    print("PLease enter name")