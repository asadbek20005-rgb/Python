password = input("Enter your password: ").lower()
security = "python123"

result = "Welcome" if password == security else "Wrong password"

print(result)