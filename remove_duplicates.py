# Program to remove duplicate elements while preserving order

# Read a list of integers
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

# Remove duplicates while preserving order using a set to track seen elements
seen = set()
unique_numbers = []

for num in numbers:
    if num not in seen:
        seen.add(num)
        unique_numbers.append(num)

# Print the result
print("Original list:", numbers)
print("List without duplicates:", unique_numbers)
