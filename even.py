"""
Program to work with even numbers
"""


def is_even(num):
    """Check if a number is even"""
    return num % 2 == 0


def filter_even_numbers(numbers):
    """Filter and return only even numbers from a list"""
    return [num for num in numbers if is_even(num)]


def get_even_numbers(start, end):
    """Generate even numbers between start and end"""
    return [num for num in range(start, end + 1) if is_even(num)]


def sum_even_numbers(numbers):
    """Calculate sum of even numbers in a list"""
    return sum(num for num in numbers if is_even(num))


# Example usage
if __name__ == "__main__":
    # Test is_even function
    print("Testing is_even():")
    print(f"4 is even: {is_even(4)}")
    print(f"7 is even: {is_even(7)}")
    print()
    
    # Test filter_even_numbers function
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original list: {numbers}")
    print(f"Even numbers: {filter_even_numbers(numbers)}")
    print()
    
    # Test get_even_numbers function
    print(f"Even numbers from 1 to 20: {get_even_numbers(1, 20)}")
    print()
    
    # Test sum_even_numbers function
    print(f"Sum of even numbers in {numbers}: {sum_even_numbers(numbers)}")
