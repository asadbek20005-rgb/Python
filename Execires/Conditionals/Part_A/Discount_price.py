prodcut_price = input("Enter price: ")

if not prodcut_price.isnumeric():
    print("Please, enter a valid price")
else:
    prodcut_price = int(prodcut_price)
    if prodcut_price < 500000:
        print("Please, enter price")
    else:
        print(f"To pay: {prodcut_price - prodcut_price * 0.10}")


