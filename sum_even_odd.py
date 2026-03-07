def main():
    # Read input from user
    input_str = input("Enter a list of integers separated by spaces: ")
    
    # Split the input string into a list of strings
    numbers_str = input_str.split()
    
    # Convert strings to integers
    try:
        numbers = [int(num) for num in numbers_str]
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")
        return
    
    # Initialize sums
    sum_even = 0
    sum_odd = 0
    
    # Calculate sums
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    # Print the results
    print(f"Sum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")

if __name__ == "__main__":
     main()