def withdraw_amount(balance,withdraw):
    if balance-withdraw>=500:
        balance=balance-withdraw
        print("withdraw successful")
        print(f"the available balance is {balance} rupees")
    else:
        print("Insufficient balance")
balance=4000
withdraw=int(input("Enter amount to withdraw: "))
withdraw_amount(balance,withdraw)