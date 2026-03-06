balance = 5000

while True:
    print("\n1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        withdraw = int(input("Enter amount to withdraw: "))
        if balance - withdraw >= 500:
            balance -= withdraw
            print("Withdrawal successful")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 2:
        print("Current balance:", balance)

    elif choice == 3:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")