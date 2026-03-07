height=int(input("Enter your height in feet: "))
if height <3:
    print("You cannot ride on the horse")
else:
    print("you can ride on the horse")
    age=int(input("Enter your age: "))
    if age <=12:
        ticket_price=150
        print(f"the ticket price:{ticket_price}")
    elif age>=13 and age<=18:
        ticket_price=250
        print(f"the ticket price:{ticket_price}")
    elif age>18:
        ticket_price=500
        print(f"the ticket price:{ticket_price}")
print("thank you")
