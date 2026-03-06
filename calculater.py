# python calculater

operater=input("Enter an operater(+ - * /): ")
n1=int(input("Enter the 1st number: "))
n2=int(input("Enter the 2nd number: "))

if operater == "+":
    result=n1+n2
    print(result)
elif operater =="-":
    result=n1-n2
    print(result)
elif operater =="*":
    result=n1*n2
    print(result)
elif operater =="/":
    result=n1/n2
    print(result)
else:print(f"{operater} is not a valid operater")
