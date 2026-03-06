age=int(input("Enter your age: "))
citizen=input("Are you am Indian citizen? (yes/no): ")
if age>=18 and citizen.lower()=="yes":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")