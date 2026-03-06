# Program to find the square root of a number

# Step 1: Import the math module
import math

# Step 2: Ask the user to enter a number
number = float(input("Enter a number to find its square root: "))

# Step 3: Check whether the number is positive or negative
if number >= 0:
    
    # Step 4: Calculate the square root using math.sqrt()
    square_root = math.sqrt(number)
    
    # Step 5: Display the result
    print("The square root of", number, "is", square_root)

else:
    
    # Step 6: If number is negative
    print("Square root cannot be calculated for negative numbers")