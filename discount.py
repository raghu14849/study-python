total_amount=int(input("Enter purchase amount: "))
if total_amount>=5000:
    discount=total_amount*0.20
elif total_amount>2000:
    discount=total_amount*0.10
else:
    discount=0
final_amount=total_amount-discount
print(f"total amount you purchase is {total_amount}")
print(f"you got {discount} discount")
print(f"the final amount you have to pay is {final_amount}")