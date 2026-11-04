secret = "python123"
guess = input("Guess the secret password: ")

if guess == secret:
    print("Welcome back!")
else:
    print("Wrong password!")
    print("Try again!")

