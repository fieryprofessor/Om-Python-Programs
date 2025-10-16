amount = int(input("Enter amount to withdraw (multiple of 10): "))
if amount % 10 != 0:
    print("Invalid amount! Must be multiple of 10.")
else:
    hundreds = amount // 100
    amount %= 100
    fifties = amount // 50
    amount %= 50
    twenties = amount // 20
    amount %= 20
    tens = amount // 10

    print("100s:", hundreds)
    print("50s:", fifties)
    print("20s:", twenties)
    print("10s:", tens)
